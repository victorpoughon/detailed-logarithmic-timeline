# /// script
# dependencies = [
#   "beautifulsoup4",
# ]
# ///

from bs4 import BeautifulSoup
import sys

def main():

    html_content = open(sys.argv[1]).read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all tables
    tables = soup.find_all('table')

    # Process each table
    for table_index, table in enumerate(tables, start=1):
        # Find the preceding <h3> tag (title for the table)
        h3_tag = table.find_previous('h3')
        h2_content = str(h3_tag) if h3_tag else f"Table {table_index}"
        
        # Print the <h2> tag for the table
        print(f"<h2>{h2_content}</h2>")
        
        # Get all rows, skipping the header row
        rows = table.find_all('tr')[1:]
        
        for row in rows:
            cells = row.find_all('td')
            
            if len(cells) == 3:
                print(f"<h3>{str(cells[0])}</h3>")
                print(f"<h4>{str(cells[1])}</h4>")
                print(f"{str(cells[2])}")
            elif len(cells) == 2:
                print(f"<h3>{str(cells[0])}</h3>")
                print(f"{str(cells[1])}")
            else:
                pass
            

if __name__ == "__main__":
    main()
