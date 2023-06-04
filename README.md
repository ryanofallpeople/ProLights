## ⚠️ **Disclaimer: Work in Progress** ⚠️

Please note that the information provided in this README might not be entirely accurate as of June 4, 2023. Certain features and functionalities mentioned herein are yet to be implemented or may have undergone changes since the last update. Kindly consider this README as a work in progress, subject to updates and improvements. We apologize for any discrepancies and encourage you to refer to the latest documentation for the most up-to-date information.

Thank you for your understanding!

---


# What is ProLights?

ProLights is a Python-based application that allows me to control the smart lights in my home studio programmatically using my Stream Deck. These lights are manufactured by Tuya and are compatible with the SmartLife app. I want to express my gratitude to the talented Jasonacox for creating the tinytuya Python module, which made this project possible. Developed entirely in Python, with the assistance of OpenAI's ChatGPT, this application started as a personal project but has now been released publicly on GitHub to learn and apply proper practices and procedures. Although a work in progress, ProLights is fully functional, and I have exciting plans to introduce even more features in the future.


# Features
* Colors are configurable by manually editing the `./config/color_config.json` file
* The color configuration file can also be generated via ChatGPT using the provided prompts.
* Included `setup.bat` automatically configures the application with the colors you provide in the `color_config.json` file
* Designed with **Stream Deck** integration in mind.

---

## Stream Deck Compatability
* Procedurally generated batch file triggers for each color in the `color_config.json` file
* Procedurally generated Stream Deck icons for each batch file trigger.
* Customizable Icon Generation
    * Adjustable amount of *Pastellness*
    * ~~Adjustable border stroke~~
    * User definable Pictogram



---


## Usage

Once the `tinytuya` configuration is complete and the `setup.bat` file has been run, using ProLights is straightforward:

1. Open the Stream Deck application and add a new `System: Open` action to a button on your Stream Deck device.

2. Navigate to the ProLights installation directory.

3. Inside the `ProLights/main/bat_triggers` folder, you will find batch files named after the colors they will set your lights to.

4. After configuring the `System: Open` action, click the small down arrow in the top left corner of the default icon image on the button.

5. Select the option labeled `Set from File`.

6. Navigate to the `ProLights/main/icons` folder and choose the icon that corresponds to the trigger you selected for the `System: Open` action.

By following these steps, you can easily control your smart lights in the home studio using the Stream Deck, triggering different lighting effects based on the batch files available in the `bat_triggers` folder. The icon selection adds a visual representation to the button, making it more intuitive and user-friendly.



---

# Installation and Setup

To use this project, you need to ensure that you have Python 3.10 or a later version installed on your system. 

1. **Python Installation:** If Python is not installed on your machine, follow the official Python installation instructions for your operating system. You can download Python from the [official Python website](https://www.python.org/downloads/).

2. **Package Installation:** After installing Python, you need to install the following packages:

   - **tinytuya:** A package for controlling Tuya devices. Install it using the following command:

     ```shell
     pip install tinytuya
     ```

   - **threading:** A built-in Python package for managing multiple threads of execution. It is included with Python by default and does not require a separate installation.

   - **concurrent:** A built-in Python package for concurrent programming. It is included with Python by default and does not require a separate installation.

   - **json:** A built-in Python package for working with JSON data. It is included with Python by default and does not require a separate installation.

   - **PIL:** The Python Imaging Library (PIL) adds image processing capabilities to your Python interpreter. Install it using the following command:

     ```shell
     pip install pillow
     ```

     Note: The package is named "Pillow" instead of "PIL" on PyPI, but you import it using `import PIL` in your code.

Once you have installed Python and the required packages, you are ready to proceed with the setup and configuration of the project.


---

## TinyTuya Configuration

Before using the `tinytuya` package, you need to configure it with the necessary credentials to communicate with Tuya devices. Follow the steps below to configure `tinytuya`:

1. **Obtain Tuya API Credentials:** To access Tuya devices through the Tuya API, you need to obtain API credentials. Refer to the Tuya API documentation or contact Tuya for instructions on how to obtain the required credentials.

2. **Configure `tinytuya`:** Once you have obtained the API credentials, you need to configure `tinytuya` with the following information:

   - **Client ID:** The client ID associated with your Tuya API credentials.
   - **Client Secret:** The client secret associated with your Tuya API credentials.
   - **Region:** The region where your Tuya devices are located.

   You can configure `tinytuya` by setting the following environment variables:

   ```shell
   export TUYA_CLIENT_ID=<your_client_id>
   export TUYA_CLIENT_SECRET=<your_client_secret>
   export TUYA_REGION=<your_region>
   ```

   Replace `<your_client_id>`, `<your_client_secret>`, and `<your_region>` with the appropriate values provided by Tuya.

   Alternatively, you can set these variables programmatically in your Python script using the `os` module.

For more information on configuring `tinytuya`, refer to the [official `tinytuya` documentation](https://pypi.org/project/tinytuya/).

Once you have configured `tinytuya` with the necessary credentials, you can proceed with using the package to control your Tuya devices.


---

## Setup Configuration

Before running the `setup.bat` file to initialize the project, you need to provide the file locations of `tinytuya.json`, `devices.json`, `tuya-raw.json`, and `snapshot.json`. This can be done by configuring the `setup.cfg` file. Follow the steps below to set up the necessary file locations:

1. **Locate the `setup.cfg` file:** The `setup.cfg` file is located in the project's root directory.

2. **Open `setup.cfg` in a text editor:** Use a text editor of your choice to open the `setup.cfg` file.

3. **Input file locations:** In the `setup.cfg` file, you will find configuration options for `tinytuya.json`, `devices.json`, `tuya-raw.json`, and `snapshot.json`. Provide the file locations for each of these files.

   ```ini
   [FileLocations]
   tinytuya_json = /path/to/tinytuya.json
   devices_json = /path/to/devices.json
   tuya_raw_json = /path/to/tuya-raw.json
   snapshot_json = /path/to/snapshot.json
   ```

   Replace `/path/to/tinytuya.json`, `/path/to/devices.json`, `/path/to/tuya-raw.json`, and `/path/to/snapshot.json` with the actual file locations on your system.

   Ensure that the files exist at the specified locations and contain the required data for your project.

4. **Save the `setup.cfg` file:** After providing the file locations, save the `setup.cfg` file.

5. **Run `setup.bat`:** Now, you can run the `setup.bat` file to initiate the project setup process. This will utilize the file locations specified in the `setup.cfg` file for further configuration.

By following these steps and configuring the `setup.cfg` file with the appropriate file locations, you will ensure that the project setup process has access to the required data files (`tinytuya.json`, `devices.json`, `tuya-raw.json`, and `snapshot.json`).

---

# TODO

- [ ] Create a `setup.cfg` file to store configuration variables and abstract them out of the codebase for better maintainability and flexibility.
- [ ] Implement an automatic mechanism to copy the `tinytuya` configuration file based on the file location specified in the `setup.cfg` file. This ensures seamless integration with the project setup process.
- [ ] Enhance the project by making the border stroke amount adjustable, allowing users to customize the visual appearance according to their preferences.
- [ ] Move the `pictogram.png` file from the `icons` folder to the project's config directory, alongside the `setup.cfg` file. This ensures a more organized and centralized location for configuration-related resources.
- [ ] Improve the setup script by incorporating error checks to validate the user's input and configurations. If any errors or issues are detected, the script should provide clear and helpful suggestions for the user's next steps, ensuring a smoother setup experience.

These items will help enhance the project's functionality, usability, and maintainability, providing a better overall experience for both developers and end users.