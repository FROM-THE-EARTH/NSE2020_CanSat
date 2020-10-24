
from typing import Dict, Tuple, Union

from pisat.comm.transceiver import SocketTransceiver

from can09.server.command_base import CommandBase
from can09.server.request import InvalidRequestError, Request


class CommandServer:
    
    def __init__(self, transceiver: SocketTransceiver, request: Request) -> None:
        self._transceiver = transceiver
        self.request = request
        self._CtoF: Dict[bytes, CommandBase] = {}             # Command to Function
    
    def append(self, *commands: Tuple[CommandBase, ...]) -> None:
        for command in commands:
            if not issubclass(command, CommandBase):
                raise TypeError(
                    "'commands' must include only CommandBase."
                )
                
            self._CtoF[command.COMMAND] = command
    
    def start_serve(self, timeout: Union[float, int] = -1.) -> None:
        if not isinstance(timeout, (float, int)):
            raise TypeError(
                "'timeout' must be float or int."
            )
        
        try:
            while True:
                sock = self._transceiver.listen(timeout)
                if sock is None:
                    break
                
                params = self.request.parse_request(sock)
                
                if params.sc_bit != self.request.SC_BIT_REQUEST:
                    raise InvalidRequestError(
                        "Invalid 'SC BIT' has been detected."
                    )
                
                command = self._CtoF.get(params.command)
                if command is None:
                    raise InvalidRequestError(
                        "Invalid command has been detected. " + 
                        f"COMMAND: {params.command}"
                    )
                
                command.exec(params)
                
        except KeyboardInterrupt:
            pass
