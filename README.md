# DCON26 Paper Hoover

## Overview
This utility automates the retrieval of PDF handouts from the DesignConCON conference portal. It facilitates the batch download of session materials to replace manual navigation and individual downloads. Tested for DesignCon 2026.

---

## Prerequisites

* **Python 3.x**
* **Playwright Library**:
    ```bash
    pip install playwright
    playwright install chromium
    ```
* **Credentials**: A `credentials.txt` file must be present in the root directory.
    * **Line 1**: Account email
    * **Line 2**: Account password

---

## Operational Workflow

1. **Authentication**: The script initializes a browser instance and navigates to the login portal.
2. **Manual Verification**: The user must manually complete the CAPTCHA and press **Enter** in the terminal to proceed.
3. **Data Loading**: The user must scroll to the bottom of the Session Gallery page to ensure all dynamic content is loaded.
4. **Extraction**: The script iterates through identified session links, navigates to the "Resources" tab, and downloads available PDFs.
5. **Organization**: Files are saved into the `Conference_Papers/` directory, sub-divided by session title. Empty directories are purged upon completion.

---

## Technical Specifications

* **Library**: Playwright (Synchronous)
* **Browser**: Chromium (Non-headless for authentication)
* **File Structure**:
    * `download_script.py`: Main execution logic.
    * `credentials.txt`: User authentication data.
    * `Conference_Papers/`: Output destination.

---

## License
MIT License.