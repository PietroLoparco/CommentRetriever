# **🛠️ Comment Retriever**  

RetrieveComment is a simple yet powerful Python tool designed to extract all HTML comments from a target webpage.  
This tool can be useful for **security researchers**, **penetration testers**, and **web analysts** looking for potential leaks or hidden information within the HTML structure.  

🚀 **Key Benefits**:  
✔️ Extracts all HTML comments from a given webpage.  
✔️ Saves the extracted comments into a specified output file.  
✔️ Displays formatted comments in the terminal for easy analysis.  

---

## **📌 Installation**  

Ensure you have the required dependencies installed:  

```bash
pip install requests beautifulsoup4 colorama
```

# 🚀 Usage
To run RetrieveComment, use the following command:

```bash
python retrieve_comment.py -T <Target_URL> -O <Output_File>
```
## 🔹 Example:
```bash
python retrieve_comment.py -T https://example.com -O comments.txt
```
# ⚙️ Arguments:

Argument	| Description
| :---: | :---: |
-T / --Target	 | Specify the target website.
-O / --OutputName	 |Set the output file name (default: Output.txt).

# 📜 Output Example
```
[0] => <!-- This is a hidden comment -->
--------------------------------------------------------

[1] => <!-- TODO: Remove debug mode before deployment -->
--------------------------------------------------------
```

⚠️ Disclaimer

This tool is intended for educational and ethical purposes only. Do not use it on websites without proper authorization. The developer is not responsible for any misuse.

📄 License
This project is licensed under the MIT License.
