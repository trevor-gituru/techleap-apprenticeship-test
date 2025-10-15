# techleap-apprenticeship-test
Technical test submission for the TechLeap Apprenticeship — includes logic, frontend, backend, and debugging solutions.


---

## 🧩 Section 1: Logic & Problem Solving
### **Q1:** [`second_largest.py`](./q1_second_largest.py)  
  
- Function to find the second largest number in a list.

**Explanation:**

The function finds the second largest number by iterating through the list a single time. Here's how it works:

1.  **Initialization**:
    *   `largest` is set to the first number in the list.
    *   `second_largest` is set to negative infinity to handle all possible numbers.

2.  **Iteration**: For each number in the list:
    *   If the number is greater than `largest`, the current `largest` becomes the `second_largest`, and the current number becomes the new `largest`.
    *   If the number is smaller than `largest` but greater than `second_largest`, it becomes the new `second_largest`.

3.  **Return Value**:
    *   After checking all the numbers, the function returns the `second_largest` value.
    *   If no `second_largest` value is found (e.g., the list has fewer than two unique numbers), it returns `None`.

**Time and Space Complexity:**

*   **Time Complexity:** `O(n)` - The list is traversed only once.
*   **Space Complexity:** `O(1)` - The memory usage is constant as it only uses a few variables, regardless of the list's size.

- Run:
```bash
razaoul@trevor-HP-650-Notebook-PC:~/techleap-apprenticeship-test$ python3 q1_second_largest.py 
5
razaoul@trevor-HP-650-Notebook-PC:~/Documents/software_dev/techleap-apprenticeship-test$
```

### **Q2:** Page Optimization

**Question:**

Explain how you would optimize a page that loads too slowly.

**Explanation:**

When a web page loads too slowly, the cause is usually a mix of large assets, inefficient code, or poor server response.
Below are three common causes and their fixes:

**1. Large Images or Media Files**

*   **Cause:** Images are uncompressed or too large for their display size.
*   **Fix:** Compress images (e.g., using TinyPNG or WebP format) and use responsive image loading (`<img srcset>` or `next/image` in Next.js).

**2. Too Many or Unoptimized HTTP Requests**

*   **Cause:** Loading too many separate CSS/JS files or third-party scripts.
*   **Fix:** Bundle and minify CSS/JS (e.g., via Webpack or Vite), defer non-critical scripts, and use lazy loading for assets.

**3. Uncached or Slow Server Responses**

*   **Cause:** Every page request hits the backend or database repeatedly.
*   **Fix:** Use browser caching, Content Delivery Networks (CDNs), and API response caching (e.g., Redis or HTTP cache headers).

## 🧩 Section 2: Web/Software Development

### **Q3:** [`q3_profile_page.js`](./q3_profile_page.js)

**Question:**

You are creating a simple profile page that fetches user data from an API (`https://jsonplaceholder.typicode.com/users/1`). Explain or show code for:

*   Fetching and displaying the user’s name and email.
*   Handling the loading and error states.

**Solution:**

The provided JavaScript code in `q3_profile_page.js` demonstrates how to solve this. It uses an `async` function and `fetch` to get the data from the API.

*   **Fetching Data**: It calls the API and waits for the response.
*   **Displaying Data**: It logs the user's name and email to the console.
*   **Error Handling**: It uses a `try...catch` block to handle potential errors, such as network issues or if the API returns an error status.

**Run:**

```bash
razaoul@trevor-HP-650-Notebook-PC:~/Documents/software_dev/techleap-apprenticeship-test$ node q3_profile_page.js 
Name: Leanne Graham
Email: Sincere@april.biz
razaoul@trevor-HP-650-Notebook-PC:~/Documents/software_dev/techleap-apprenticeship-test$
```

### **Q4:** [`q4_total_sales.py`](./q4_total_sales.py)

**Question:**

A small store wants to calculate total sales from this dataset:
```json
[
  {"item": "Pen", "price": 20, "quantity": 3},
  {"item": "Book", "price": 200, "quantity": 2},
  {"item": "Bag", "price": 800, "quantity": 1}
]
```
Write a short function to calculate the total revenue.

**Solution:**

The Python script `q4_total_sales.py` contains a function that iterates through the list of sales data. For each item, it multiplies the `price` by the `quantity` and adds it to a running total. The final total is then printed.

**Run:**

```bash
razaoul@trevor-HP-650-Notebook-PC:~/Documents/software_dev/techleap-apprenticeship-test$ python3 q4_total_sales.py 
Total sales: 1260
razaoul@trevor-HP-650-Notebook-PC:~/Documents/software_dev/techleap-apprenticeship-test$ 

```

## 🧩 Section 3: Debugging & Reasoning

### **Q5:** [`q5_debugging_fix.py`](./q5_debugging_fix.py)

**Question:**

You’ve been given this code snippet:
```python
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    if i % 2 == 0:
        numbers.remove(i)
print(numbers)
```

*   What’s wrong with the code?
*   What will it output?
*   How would you fix it to remove even numbers correctly?

**Analysis:**

*   **What’s wrong with the code?**
    When it comes to removing the even number, it doesnt check if the even number exists in the list before trying to remove it. 

*   **What will it output?**
    The code will raise a `ValueError`. On the first iteration, `i` is `0`. The condition `i % 2 == 0` is true, and the code tries to execute `numbers.remove(0)`. However, the value `0` is not present in the `numbers` list `[1, 2, 3, 4, 5]`, causing a `ValueError`.

*   **How would you fix it?**
    A safe and efficient way to remove elements from a list is to create a new list containing only the even elements. The corrected code is in `q5_debugging_fix.py`.

**Run the fixed code:**

```bash
razaoul@trevor-HP-650-Notebook-PC:~/Documents/software_dev/techleap-apprenticeship-test$ python3 q5_debugging_fix.py 
[1, 3, 5]
razaoul@trevor-HP-650-Notebook-PC:~/Documents/software_dev/techleap-apprenticeship-test$ 

```

## 🧩 Section 4: Version Control & Collaboration

### **Q6:** Git Collaboration

**Question:**

Explain how you would use Git to collaborate on a team project with other developers. Mention at least:

*   One common Git command you use often.
*   One problem you’ve faced while using Git and how you solved it.

**Solution:**

A common and effective way to collaborate using Git is the **feature branching workflow**. This keeps the `main` branch stable by having developers create separate branches for each new feature or bugfix.

Here’s a demonstration of creating a feature branch, making a commit, and merging it back into the `main` branch:

```bash
# Start on the main branch
razaoul@trevor-HP-650-Notebook-PC:~/Documents/software_dev/techleap-apprenticeship-test$ git branch -v
* main 91cd24d Added Q1 - Q5 solutions

# Create a new branch for a new feature and switch to it
razaoul@trevor-HP-650-Notebook-PC:~/Documents/software_dev/techleap-apprenticeship-test$ git checkout -b second
Switched to a new branch 'second'

# Add a new file and commit the changes to the new branch
razaoul@trevor-HP-650-Notebook-PC:~/Documents/software_dev/techleap-apprenticeship-test$ git add "Apprenticeship Entry Test.md"
razaoul@trevor-HP-650-Notebook-PC:~/Documents/software_dev/techleap-apprenticeship-test$ git commit -m "Added apprenticeship test questions"
[second 6bb9067] Added apprenticeship test questions
 1 file changed, 59 insertions(+)
 create mode 100644 "Apprenticeship Entry Test.md"

# Switch back to the main branch
razaoul@trevor-HP-650-Notebook-PC:~/Documents/software_dev/techleap-apprenticeship-test$ git checkout main
Switched to branch 'main'

# Merge the feature branch into main
razaoul@trevor-HP-650-Notebook-PC:~/Documents/software_dev/techleap-apprenticeship-test$ git merge second
Updating 91cd24d..6bb9067
Fast-forward
 "Apprenticeship Entry Test.md" | 59 +++++++++++++++++++++++++++++++
 1 file changed, 59 insertions(+)
 create mode 100644 "Apprenticeship Entry Test.md"
```

**1. Common Git Command**

A command I use constantly is `git checkout -b <branch-name>`. It's a powerful shortcut that creates a new branch and immediately switches to it, allowing me to quickly start working on a new task without affecting the main codebase.

**2. Problem Faced: Merge Conflicts**

A common problem is a **merge conflict**, which happens when Git can’t automatically combine changes from two different branches because they affect the same lines in the same file.

*   **How I solve it:**
    1.  When Git indicates a merge conflict, I open the conflicted file.
    2.  Git marks the conflicting sections with `<<<<<<<`, `=======`, and `>>>>>>>`. I manually edit the file to resolve the differences, keeping the code I want and removing the conflict markers.
    3.  Once the file is corrected, I use `git add <filename>` to stage the resolved file.
    4.  Finally, I run `git commit` to complete the merge.
