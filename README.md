# 2024 Favorite Programming Language Voting App

Welcome to the 2024 Favorite Programming Language Voting App! This application allows users to vote for their favorite programming languages.

**View and vote on the live app** [here](https://serverless-voting.netlify.app/)

## Features

- **Vote for Your Favorite Language:** Users can vote for their preferred programming languages.
- **Interactive Design:** The app has an interactive and visually appealing design.

## Technologies Used

- **Frontend:** React
- **Backend:** AWS Lambda, DynamoDB
- **Styling:** Tailwind CSS
- **Deployment:** AWS API Gateway for backend, Netlify for frontend

![Untitled(1)](https://github.com/Mohd-Daniyal/Serverless-Voting-Application/assets/96229438/df51bbd4-3869-48d0-9995-0852440d0112)


## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies:**
   ```bash
   npm install
   ```

3. **Run the App:**
   ```bash
   npm start
   ```

   The app should now be running on http://localhost:3000.

## AWS Setup

- **Lambda Function:** The AWS Lambda function handles the backend logic for voting.
- **DynamoDB:** The app uses DynamoDB to store and retrieve language data.

## API Endpoints

- `/languages`: Fetches the list of programming languages.
- `/languages/{language}`: Fetches details of a specific language.
- `/languages/{language}/vote`: Handles voting for a specific language.

### Lambda Function Mapping

- **Function 1: GetAllVotes**
  - **Endpoint:** `/languages`
  - **Description:** Retrieves the list of programming languages with their details from DynamoDB.

- **Function 2: GetLanguageInfo**
  - **Endpoint:** `/languages{language}`
  - **Description:** Retrieves the information of a particular programming language from DynamoDB.

- **Function 3: VoteCountUpdate**
  - **Endpoint:** `/languages/{language}/vote`
  - **Description:** Increments the vote count for the specified language in DynamoDB.

Feel free to make any further adjustments or let me know if there's anything else you'd like to add!
