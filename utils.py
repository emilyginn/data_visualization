##################### BUILD TABLES FROM WEB SCRAPING #####################

def extract_headers(rows):
    for row in rows:
        headers = row.find_all('th')
        header_texts = [header.text.strip() for header in headers]
        if header_texts:
            return header_texts
        
def extract_cells(rows):
    output_cells = []
    cells = []

    for row in rows:
        find_cells = row.find_all('td')
        cell_data = []
        for cell in find_cells:
            text = cell.get_text(strip=True)
            cell_data.append(text)
        cells.append(cell_data)

    # Print the data
    for cell_data in cells:
        if cell_data:
            output_cells.append(cell_data)
            
    return output_cells

def build_table(rows):
    return pd.DataFrame(extract_cells(rows), columns=extract_headers(rows))