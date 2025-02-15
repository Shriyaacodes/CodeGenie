LANGUAGE_CONFIGS = {
    "Python": {
        "file_ext": ".py",
        "common_imports": [
            "import os",
            "import sys",
            "from datetime import datetime",
            "import json"
        ]
    },
    "Java": {
        "file_ext": ".java",
        "common_imports": [
            "import java.util.*;",
            "import java.io.*;",
            "import java.time.*"
        ]
    },
    "C++": {
        "file_ext": ".cpp",
        "common_imports": [
            "#include <iostream>",
            "#include <vector>",
            "#include <string>"
        ]
    },
    "C": {
        "file_ext": ".c",
        "common_imports": [
            "#include <stdio.h>",
            "#include <stdlib.h>",
            "#include <string.h>"
        ]
    }
}

def format_code_prompt(prompt, language):
    """Format the prompt for code generation."""
    config = LANGUAGE_CONFIGS.get(language, LANGUAGE_CONFIGS["Python"])

    return f"""
Please generate {language} code for the following task:

Task Description:
{prompt}

Requirements:
- Use {language} best practices and conventions
- Include necessary imports/includes
- Add comments explaining complex logic
- Handle common edge cases
- Follow standard {language} code style

Common {language} imports that might be useful:
{chr(10).join(config['common_imports'])}

Please provide the complete, working code in {language}:
"""

def format_explanation_prompt(code, language):
    """Format the prompt for code explanation."""
    return f"""
Please provide a detailed explanation of the following {language} code:

{code}

Please include:
1. Overall purpose and functionality
2. Breakdown of key components and their roles
3. Explanation of any complex algorithms or logic
4. Notable design patterns or techniques used
5. Potential performance considerations
6. Any important edge cases or limitations

Format the explanation in clear, readable markdown.
"""

def format_debug_prompt(code, language):
    """Format the prompt for code debugging."""
    return f"""
Please analyze and debug the following {language} code:

{code}

Please provide:
1. Identification of potential bugs and issues
2. Code quality concerns
3. Performance optimization opportunities
4. Security considerations
5. Suggested fixes and improvements
6. Corrected version of the code in {language}

Format the response in clear, readable markdown with code examples where appropriate.
"""

def format_optimize_prompt(code, language):
    """Format the prompt for code optimization."""
    return f"""
Please optimize the following {language} code for better performance and efficiency:

{code}

Please provide:
1. Identification of performance bottlenecks
2. Suggested optimizations and improvements
3. Optimized version of the code in {language}

Format the response in clear, readable markdown with code examples where appropriate.
"""

def format_complexity_prompt(code, language):
    """Format the prompt for complexity estimation."""
    return f"""
Please estimate the time complexity of the following {language} code:

{code}

Please provide:
1. An estimation of the time complexity (e.g., O(n), O(n log n))
2. Explanation of the reasoning behind the estimation
3. Any assumptions made during the estimation

Format the response in clear, readable markdown.
"""

def get_language_config(language):
    """Get the configuration for a specific language."""
    return LANGUAGE_CONFIGS.get(language, LANGUAGE_CONFIGS["Python"])

def get_basic_syntax(language):
    """Get the basic syntax for a specific language."""
    basic_syntax = {
        "Python": """
# Basic Python Syntax
print("Hello, World!")

# Variables
x = 5
y = "Hello"

# Conditional Statements
if x > 0:
    print("x is positive")

# Loops
for i in range(5):
    print(i)

while x > 0:
    print(x)
    x -= 1

# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
""",
        "Java": """
// Basic Java Syntax
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

// Variables
int x = 5;
String y = "Hello";

// Conditional Statements
if (x > 0) {
    System.out.println("x is positive");
}

// Loops
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

while (x > 0) {
    System.out.println(x);
    x--;
}

// Functions
public static String greet(String name) {
    return "Hello, " + name + "!";
}

System.out.println(greet("Alice"));
""",
        "C++": """
// Basic C++ Syntax
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}

// Variables
int x = 5;
std::string y = "Hello";

// Conditional Statements
if (x > 0) {
    std::cout << "x is positive" << std::endl;
}

// Loops
for (int i = 0; i < 5; i++) {
    std::cout << i << std::endl;
}

while (x > 0) {
    std::cout << x << std::endl;
    x--;
}

// Functions
std::string greet(std::string name) {
    return "Hello, " + name + "!";
}

std::cout << greet("Alice") << std::endl;
""",
        "C": """
// Basic C Syntax
#include <stdio.h>

int main() {
    printf("Hello, World!\\n");
    return 0;
}

// Variables
int x = 5;
char y[] = "Hello";

// Conditional Statements
if (x > 0) {
    printf("x is positive\\n");
}

// Loops
for (int i = 0; i < 5; i++) {
    printf("%d\\n", i);
}

while (x > 0) {
    printf("%d\\n", x);
    x--;
}

// Functions
char* greet(char* name) {
    static char message[50];
    sprintf(message, "Hello, %s!", name);
    return message;
}

printf("%s\\n", greet("Alice"));
"""
    }
    return basic_syntax.get(language, basic_syntax["Python"])
