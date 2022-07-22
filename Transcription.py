def RNA():
    DNA_sample = (input("Enter the DNA sequence to be transcribed: "))
    transcript = DNA_sample.maketrans("ATGC", "TUCG")
    print(DNA_sample.translate(transcript))
    
    
def pos():
        
    DNA_genome = input("Enter the sample sequence: ")
    position = DNA_genome.find(input("Enter the seq to find: "))
    print(position)
    
x = input("Enter the function: ")
if x == "transcription":
    print(RNA())
elif x == "position":
    print(pos())



    
    
        
        

        
    
    
    
