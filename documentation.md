## Users App Endpoints

This documentation provides an overview of the available endpoints in the Users app.

### API Endpoints

#### List Mac Addresses

- **URL:** `/api-list-mac-address/`
- **Method:** GET
- **Description:** Retrieves a list of Mac Addresses.
- **Response:** Returns a JSON array containing Mac Address objects.

#### List Telegram Bots

- **URL:** `/api-list-bots/`
- **Method:** GET
- **Description:** Retrieves a list of Telegram Bots.
- **Response:** Returns a JSON array containing Telegram Bot objects.

#### Check Mac Address Existence

- **URL:** `/api-check-exist/<str:mac_address>`
- **Method:** GET
- **Description:** Checks if a Mac Address exists.
- **Response:** Returns a JSON object indicating whether the Mac Address exists.

#### Get Telegram Bot URL

- **URL:** `/bot-url/<str:name>`
- **Method:** GET
- **Description:** Retrieves the URL of a Telegram Bot.
- **Response:** Returns a JSON object containing the URL of the Telegram Bot.

#### Check Mac Address Existence (Alternative)

- **URL:** `/api-check-exist/`
- **Method:** POST
- **Description:** Checks if a Mac Address exists.
- **Request Body:** Expects a JSON object with the following field:
  - `mac_address` (string): The Mac Address to check.
- **Response:** Returns a JSON object indicating whether the Mac Address exists.

#### Get Chat IDs by Bot Name

- **URL:** `/api-chats/<str:name>`
- **Method:** GET
- **Description:** Retrieves the Chat IDs associated with a given Telegram Bot.
- **Response:** Returns a JSON array containing the Chat IDs.

### Additional Notes

- Make sure to include the app's URLs in your project's main `urls.py` file using the `include` function.
- Some endpoints require specific parameters in the URL or request body.
- Ensure that you have the appropriate permissions and authentication set up for accessing the endpoints.

Please note that this is only a sample documentation, and you should customize it further based on your specific requirements, including details about the request and response payloads, authentication, and any additional information relevant to your API.