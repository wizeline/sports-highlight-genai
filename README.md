# Project

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## Table of Contents

- [Description](#description) :pencil2:
- [Contributing](#contributing)
- [License](#license) :page_with_curl:
- [Authors](#authors) :busts_in_silhouette:

___
## Description

Develop a GenAI-powered tool that automatically identifies key moments in sports events to generate highlight reels. This project leverages real-time statistical data, video processing, and image analysis to create engaging sports highlights. Optional features include video editing capabilities and social media integration for sharing highlights.

___

## Project Structure

```plaintext
input_files/                  # Directory for input files
output_files/                 # Directory for output files
    __init__.py               # Initialization file for output files package
src/                          # Source code directory
    app.py                    # Main application entry point
    config.py                 # Configuration settings for the project
    handlers/                 # Directory for handler modules
        __pycache__/          # Compiled Python files for handlers
        __init__.py           # Initialization file for handlers package
        data_management.py    # Data processing and management functions
        facebook_api.py       # Facebook API integration
        tiktok_api.py         # TikTok API integration
        instagram_api.py      # Instagram API integration
        youtube_api.py        # YouTube API integration
        video_processing.py   # Video processing functions
    services/                 # Directory for service modules
        __pycache__/          # Compiled Python files for services
        __init__.py           # Initialization file for services package
        mlb_api.py            # MLB API integration
        aws_s3.py             # AWS S3 integration
        authentication.py     # Authentication services
    utils/                    # Directory for utility modules
        __pycache__/          # Compiled Python files for utilities
        __init__.py           # Initialization file for utilities package
        file_export.py        # File export utilities
        helpers.py            # Helper functions
        logger.py             # Logging utilities
    tests/                    # Directory for test modules
        __pycache__/          # Compiled Python files for tests
        __init__.py           # Initialization file for tests package
        test_facebook_api.py  # Tests for Facebook API integration
        test_tiktok_api.py    # Tests for TikTok API integration
        instagram_api.py      # Tests for Instagram API integration
        youtube_api.py        # Tests for YouTube API integration
        test_authentication.py# Tests for authentication services
        test_aws_s3.py        # Tests for AWS S3 integration
        test_video_processing.py # Tests for video processing functions
        test_data_management.py  # Tests for data management functions
        test_mlb_api.py       # Tests for MLB API integration
.gitignore                    # Git ignore file
README.md                     # Project documentation
.env                          # Environment variables configuration
requirements.txt              # Python dependencies
setup.py 
```

___
## Contributing

-Guidelines for contributing to the project. Include how to clone the repository, create a branch, make commits, and submit pull requests.

- [ ] Fork the project
- [ ] Create your Feature Branch (`git checkout -b feature/new-feature`)
- [ ] Commit your changes (`git commit -m 'Add new feature'`)
- [ ] Push to the branch (`git push origin feature/new-feature`)
- [ ] Open a Pull Request

___
## License
This project is licensed under the MIT License. See the LICENSE file for details.

___
## Authors

* **@author:** Fabián Portillo González 
* **@github user:** fabianpg95
* **@author:** Narda Ballesteros
* **@github user:** NardaBallesterosW
* **@author:** Fernanda Meza
* **@github user:** fernanda-meza-wizeline
* **@author:** José Manuel Hidalgo
* **@github user:** JoseHidalgoW
___