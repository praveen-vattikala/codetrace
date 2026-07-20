from agent.cli import run

SAMPLE_PROMPTS = [
    "write a function to reverse a string",
    "write a function to check if a number is prime",
    "write a function that checks if a string is a palindrome",
    "write a function to find the factorial of a number",
    "write a function to sort a list of dictionaries by a key",
    "write a function to remove duplicates from a list",
    "write a function to count word frequency in a string",
    "write a function to flatten a nested list",
    "write a function to check if two strings are anagrams",
    "write a function to find the largest number in a list",
    "write a function to convert a list of tuples into a dictionary",
    "write a function to validate an email address using regex",
    "write a function to merge two sorted lists",
    "write a function to calculate the fibonacci sequence up to n",
    "write a function to read a csv file using pandas",
]

for prompt in SAMPLE_PROMPTS:
    run(prompt)