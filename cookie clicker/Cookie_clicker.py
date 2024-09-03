from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# Set up the Chrome WebDriver
ser_obj = Service("C:/Users/crmsm/OneDrive - St Pauls School/chromedriver-win32/chromedriver.exe")
options = Options()
options.add_argument("user-data-dir=C:/Users/crmsm/AppData/Local/Google/Chrome/User Data")  # Adjust the path
options.add_argument("profile-directory=Default")  # Use your profile directory

driver = webdriver.Chrome(service=ser_obj, options=options)


# Function to load game state from a file
def load_game_state():
    try:
        with open("game_state.json", "r") as file:
            state = json.load(file)
            return state
    except FileNotFoundError:
        return None


# Function to save game state to a file
def save_game_state(state):
    with open("game_state.json", "w") as file:
        json.dump(state, file)


# Load the previous game state
game_state = load_game_state()

# Navigate to the Cookie Clicker website
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()

# Wait for the page to fully load
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "bigCookie"))
    )

    # If there is a saved game state, apply it
    if game_state:
        driver.execute_script(f"Game.LoadSave('{game_state['save_string']}');")

    # Inject the auto-clicker JavaScript code
    auto_clicker_script = """
    var autoclicker = setInterval(function(){
      try {
        Game.lastClick -= 1000;
        document.getElementById('bigCookie').click();
      } catch (err) {
        console.error('Stopping auto clicker');
        clearInterval(autoclicker);
      }
    }, 1);
    """
    driver.execute_script(auto_clicker_script)

    # Example: Save the game state every 30 seconds
    while True:
        time.sleep(10)
        # Get the current game save string
        save_string = driver.execute_script("return Game.WriteSave(1);")
        save_game_state({"save_string": save_string})

finally:
    # Wait for user input to close the browser
    input("Press Enter to close the browser and stop the auto clicker...")

    # Close the browser
    driver.quit()
