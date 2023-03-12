from rich.console import Console
from rich import text

class Debug:

    def __init__(self, message : str) -> None:
        
        self.__message = message
        self.__console = Console()
        
        self.__console.print(self.__message)
        
        pass

    

class Flag(Debug) :

    def __init__(self, message: str, code_line : int) -> None:
        
        self.__message = text.Text("[Flag] ", style="yellow")
        self.__message += text.Text("line: ",style="white")
        self.__message += text.Text(f"{code_line} ",style="blue")
        self.__message += text.Text(">>> ", style="yellow")
        self.__message += message

        super().__init__(self.__message)



        


if __name__ == "__main__":

    Flag("Prueba de texto",37)


