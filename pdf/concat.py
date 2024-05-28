import os
from PyPDF2 import PdfReader, PdfWriter

def list_pdfs(folder):
    """List all PDF files in the specified folder."""
    return [file for file in os.listdir(folder) if file.endswith('.pdf')]

def choose_order(files, language):
    """Allow the user to choose the order of the PDF files."""
    if language == 'fr':
        print("Fichiers PDF trouvés :")
    else:
        print("Found PDF files:")
    
    for index, file in enumerate(files, 1):
        print(f"{index}. {file}")
    
    if language == 'fr':
        order = input("Entrez l'ordre des fichiers à concaténer (ex: 1 3 2): ")
    else:
        order = input("Enter the order of files to concatenate (e.g., 1 3 2): ")
    
    indices = [int(i) - 1 for i in order.split()]
    return [files[i] for i in indices]

def concatenate_pdfs(file_list, output):
    """Concatenate PDF files into a single file."""
    pdf_writer = PdfWriter()

    for file in file_list:
        pdf_reader = PdfReader(file)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output, 'wb') as out_pdf:
        pdf_writer.write(out_pdf)

def main():
    print("Choose your language / Choisissez votre langue [EN/FR]: ")
    language = input().lower()
    while language not in ['en', 'fr']:
        print("Invalid input. Please enter 'EN' for English or 'FR' for French.")
        language = input().lower()
    
    current_folder = '.'
    pdf_files = list_pdfs(current_folder)
    
    if not pdf_files:
        if language == 'fr':
            print("Aucun fichier PDF trouvé dans le répertoire courant.")
        else:
            print("No PDF files found in the current directory.")
        return
    
    chosen_files = choose_order(pdf_files, language)
    if language == 'fr':
        output_file_name = input("Entrez le nom du fichier PDF de sortie : ")
    else:
        output_file_name = input("Enter the name of the output PDF file: ")
    
    concatenate_pdfs(chosen_files, output_file_name)
    if language == 'fr':
        print(f"Les fichiers ont été concaténés dans {output_file_name}")
    else:
        print(f"Files have been concatenated into {output_file_name}")

if __name__ == "__main__":
    main()
