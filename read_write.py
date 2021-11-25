import sys

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    zadanie = next_line(the_file)
    pustota = next_line(the_file)
    podskazka1 = next_line(the_file)
    podskazka2 = next_line(the_file)
    podskazka3 = next_line(the_file)
    podskazka4 = next_line(the_file)
    podskazka5 = next_line(the_file)
    a = next_line(the_file)
    b = next_line(the_file)
    c = next_line(the_file)   

     
   

    return zadanie, pustota, podskazka1, podskazka2, podskazka3, podskazka4,podskazka5, a,b,c


 
def main():
    text_file1 = open("print.txt", "w") 
    text_file2 = open("Новый текстовый документ.txt", "r")
    
   
    # get first block
    zadanie, pustota, podskazka1, podskazka2, podskazka3,podskazka4,podskazka5, a,b,c = next_block(text_file2)
    while zadanie:
        
        
        text_file1.write ('м3.13.2.12-2\n')
        
        text_file1.write (zadanie[zadanie.find('Запиши'):zadanie.find('«')-1]+zadanie[zadanie.find('»'):zadanie.find(':')]+'.\n')
        text_file1.write ('\n')
        text_file1.write ('###**'+zadanie[zadanie.find('«'):zadanie.find('»')+1]+'**\n')
        text_file1.write ('**Решение:**\n')
        text_file1.write ('<br><br>\n')
        text_file1.write ('\n')
        text_file1.write ('«**'+zadanie[zadanie.find('«'):zadanie.find('»')+1]+'**».\n')
        text_file1.write (podskazka4)
        text_file1.write ('\n')
        text_file1.write (podskazka5)
        text_file1.write ('{{right-answer:}}\n')
        
       

        # get next block
        zadanie, pustota, podskazka1, podskazka2, podskazka3,podskazka4,podskazka5, a,b,c = next_block(text_file2)
    
    text_file1.close()
    text_file2.close()

    print("That was the last question!")

  

main()


input("\n\nPress the enter key to exit.")

