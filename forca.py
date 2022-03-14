'''''
classe responsavel por mostrar a forca
'''
class Forca:


    def __init__(self):
        pass

    
    
    forca1 = (''''
        -------
        |     |
        |
        |
        |
        |
            '''
    ,''''
        -------
        |     |
        |     o
        |
        |
        |
            '''
    ,''''
        -------
        |     |
        |     o
        |     |
        |
        |
            '''
    ,''''
        -------
        |     |
        |     o
        |    /|
        |
        |
            '''
    ,''''
        -------
        |     |
        |     o
        |    /|\\
        |
        |
            '''
    ,''''
        -------
        |     |
        |     o
        |    /|\\      
        |    /
        |
            '''
    ,''''
        -------
        |     |
        |     o
        |    /|\\      
        |    / \\
        |
    ''')

    def mostrar(self,numero):
        print(self.forca1[numero])