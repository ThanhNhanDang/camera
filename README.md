# Multi-Camera Capture for Odoo 17

## Overview

The **Multi-Camera Capture** module enhances the `res.partner` model in Odoo 17 by adding multi-camera functionality. This feature allows users to capture and store images from multiple cameras directly within the Odoo interface.

## Features

- **Multiple Camera Integration**: Supports up to four cameras for capturing images simultaneously.
- **Flexible Image Fields**: Captured images are stored in the following fields:
  - `image_1920_1`: Top View
  - `image_1920_2`: Bottom View
  - `image_1920_3`: Left View
  - `image_1920_4`: Right View
- **User-Friendly Interface**:
  - A new "Camera Capture" page is added to the `res.partner` form view.
  - Select cameras and preview live feeds within the modal.
- **Image Capture and Storage**: Captures snapshots from live camera feeds and saves them directly to the corresponding image fields in the Odoo record.
- **Dynamic Camera Selection**: Automatically detects and lists available video input devices for user selection.

## Usage

1. Navigate to the **Camera Capture** tab in the partner form view.
2. Click the "Capture" button to open the camera modal.
3. Use the dropdown menus to select cameras for each view (Top, Bottom, Left, Right).
4. Preview live video feeds from the selected cameras.
5. Capture images using the "Capture" button.
6. Images are automatically saved to the corresponding fields.

## License

This module is licensed under the LGPL-3.

## Contact

For support or inquiries, contact: **yesthanhnhan16@gmail.com**
