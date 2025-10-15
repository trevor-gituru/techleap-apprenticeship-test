/**
 * Fetches user data from a public API and logs the user's name and email.
 *
 * @async
 * @function getUser
 * @returns {Promise<void>} 
 *          A Promise that resolves when the API call completes.
 *          Logs the user's name and email to the console if successful,
 *          or logs an error message if the request fails.
 *
 * @example
 * // Expected console output:
 * // Name: Leanne Graham
 * // Email: Sincere@april.biz
 *
 * getUser();
 */
async function getUser() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/users/1");
    if (!response.ok) throw new Error("Request failed with status " + response.status);
    const data = await response.json();
    console.log("Name:", data.name);
    console.log("Email:", data.email);
  } catch (err) {
    console.error("Error:", err.message);
  }
}

await getUser();
