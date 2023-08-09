
actions=["Add", "Update", "Retrieve", "Upload", "Download"]
file_type=["csv", "json", "xml"]



minimum_char=12

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
'''
    "\n",
    "print(\"Welcome to the PyPassword Generator!\")\n",
    "nr_letters= int(input(\"How many letters would you like in your password?\\n\")) \n",
    "nr_symbols = int(input(f\"How many symbols would you like?\\n\"))\n",
    "nr_numbers = int(input(f\"How many numbers would you like?\\n\"))\n",
    "\n",
    "\n",
    "password_char=[]\n",
    "\n",
    "for n in range(0,nr_letters):\n",
    "  password_char.append(random.choice(letters)) \n",
    "for n in range(0,nr_symbols):\n",
    "  password_char.append(random.choice(symbols)) \n",
    "for n in range(0,nr_numbers):\n",
    "  password_char.append(random.choice(numbers)) \n",
    "\n",
    "\n",
    "print(password_char)\n",
    "\n",
    "random.shuffle(password_char)\n",
    "\n",
    "print(password_char)\n",
    "\n",
    "\n",
    "my_password=\"\"\n",
    "\n",
    "for char in password_char:\n",
    "    my_password += char\n",
    "    \n",
    "print(my_password)"
   ]
  },
  {
'''