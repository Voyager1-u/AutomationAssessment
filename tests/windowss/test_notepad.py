

import sys
import os
import time
import subprocess

from pywinauto import Desktop
from pywinauto.keyboard import send_keys


# Project root path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../")
    )
)

from utils.logger import get_logger


logger = get_logger("windows_notepad_logs")


def test_notepad_automation():

    logger.info("START: Notepad Automation Test")

    # Dynamic file name
    file_name = f"TestFile_{int(time.time())}.txt"

    file_path = os.path.join(
        os.getcwd(),
        file_name
    )

    logger.info(f"Generated File Name: {file_name}")

    expected_text = """Hello Uday
This is Windows Automation Testing
Using Pywinauto Framework"""

    logger.info("Opening Notepad")

    subprocess.Popen("notepad.exe")

    time.sleep(3)

    desktop = Desktop(backend="uia")

    logger.info("Connecting to Notepad window")

    notepad = desktop.window(
        title_re=".*Notepad.*",
        found_index=0
    )

    notepad.wait("visible", timeout=20)

    notepad.set_focus()

    time.sleep(2)

    logger.info("Locating editor area")

    try:
        editor = notepad.child_window(control_type="Document")

    except:
        editor = notepad.child_window(control_type="Edit")

    editor.click_input()

    logger.info("Typing multiline text")

    editor.type_keys(
        "Hello Uday{ENTER}"
        "This is Windows Automation Testing{ENTER}"
        "Using Pywinauto Framework",
        with_spaces=True
    )

    time.sleep(2)

    logger.info("Opening Save As dialog")

    send_keys("^+s")

    time.sleep(3)

    logger.info(f"Entering filename: {file_name}")

    send_keys(file_name)

    time.sleep(1)

    logger.info("Saving file")

    send_keys("{ENTER}")

    time.sleep(3)

    # Handle overwrite popup
    try:
        logger.info("Checking overwrite popup")

        overwrite = desktop.window(
            title_re=".*Confirm Save As.*",
            found_index=0
        )

        overwrite.wait("visible", timeout=5)

        send_keys("{LEFT}")

        send_keys("{ENTER}")

        logger.info("Overwrite confirmed")

    except:
        logger.info("No overwrite popup appeared")

    time.sleep(2)

    logger.info("Validating file exists")

    assert os.path.exists(file_path)

    logger.info("Closing first Notepad")

    notepad.close()

    time.sleep(2)

    logger.info("Reopening saved file")

    subprocess.Popen([
        "notepad.exe",
        file_path
    ])

    time.sleep(5)

    logger.info("Connecting to reopened Notepad")

    reopened = desktop.window(
        title_re=".*Notepad.*",
        found_index=0
    )

    reopened.wait("visible", timeout=20)

    reopened.set_focus()

    time.sleep(2)

    logger.info("Reading saved content")

    try:
        editor2 = reopened.child_window(
            control_type="Document"
        )

        editor2.wait("ready", timeout=10)

    except:
        editor2 = reopened.child_window(
            control_type="Edit"
        )

        editor2.wait("ready", timeout=10)

    actual_text = editor2.window_text()

    # Text normalization
    def normalize_text(text):
        return (
            text
            .replace("\r\r\n", "\n")
            .replace("\r\n", "\n")
            .replace("\r", "\n")
            .strip()
        )

    actual_text = normalize_text(actual_text)

    expected_text = normalize_text(expected_text)

    logger.info("Validating text content")

    assert expected_text == actual_text, (
        f"\nExpected:\n{repr(expected_text)}"
        f"\nActual:\n{repr(actual_text)}"
    )

    logger.info("Closing reopened file")

    reopened.close()

    time.sleep(1)

    logger.info("Deleting created file")

    os.remove(file_path)

    logger.info("END: Notepad Automation Test PASSED")