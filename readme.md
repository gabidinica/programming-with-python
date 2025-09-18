# Demo Project: Automation with Python

## Technologies Used
- Python
- IntelliJ
- Git

## Project Description
Develop an application that can **read a spreadsheet file** and perform **processing and manipulation** on the spreadsheet data. The program should be able to handle tasks such as extracting information, updating values, and modifying the structure of the spreadsheet.

---

The program should implement the following logic:

### Features
1. **Products per Supplier**  
   - Calculate how many products are supplied by each company.  
   - Output: List of each supplier with the respective product count.  

2. **Low Inventory Products**  
   - Identify products that have an inventory count of **less than 10**.  
   - Output: List of these products.  

3. **Total Inventory Value per Supplier**  
   - Calculate the **total inventory value** for each supplier.  
   - Output: List of suppliers with their respective total inventory value.  

4. **Write Back to Spreadsheet**  
   - For each product, calculate its **inventory value** (`inventory * price`).  
   - Write this value back into the spreadsheet under a new column.  

**NOTE** We're gonna use the inventory.xlsx file.

## Working with Spreadsheets

- The file **`inventory.xlsx`** should exist in the project folder.  
- To work with spreadsheets, we are using **[openpyxl](https://pypi.org/project/openpyxl/)** from PyPI.  
- Install the library by running the following command in the terminal:  

```bash
pip install openpyxl
```

*Expected result*: 
{
    'AAA Company': 43,
    'BBB Company': 17,
    'CCC Company': 56
}

To set a value in a new column for the last scenario (**calculate and write inventory value for each product**), we can use the following code:  

```python
inventory_price.value = inventory * price
```

> ⚠️ This updates the value in memory, but it does not save the file yet.

To save the updated spreadsheet under a new name (inventory_with_total_value.xlsx), use:
``` bash
inv_file.save('inventory_with_total_value.xlsx')
```

