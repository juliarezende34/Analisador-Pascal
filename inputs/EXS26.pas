program ConstantesHexadecimais;

const
  // Constantes em hexadecimal
  MASCARAvERMELHA := 0xFF0000;     
  MASCARAvERDE    := 0x00FF00;     
  MASCARAaZUL     := 0x0000FF;     
  FLAGaTIVO       := 0x01;         
  FLAGvISIVEL     := 0x02;         
  FLAGeDITAVEL    := 0x04;         
  NUMEROmAGICO    := 0xDEADBEEF;

var
  cor: integer;
  flags: byte;
  valor: cardinal;

// Função para extrair componentes de cor RGB
procedure ExtrairComponentesRGB(cor: integer);
var
  vermelho, verde, azul: byte;
begin
  vermelho := (cor and MASCARAvERMELHA) shr 16;
  verde := (cor and MASCARAvERDE) shr 8;
  azul := cor and MASCARAaZUL;
  
  writeln('Componentes RGB:');
  writeln('Vermelho: ', vermelho);
  writeln('Verde:    ', verde);
  writeln('Azul:     ', azul);
end;

// Função para verificar flags
procedure VerificarFlags(flags: byte);
begin
  writeln('Status:');
  writeln('Ativo:    ', (flags and FLAGaTIVO) <> 0);
  writeln('Visível:  ', (flags and FLAGvISIVEL) <> 0);
  writeln('Editável: ', (flags and FLAGeDITAVEL) <> 0);
end;

begin
  writeln('Número mágico: ', NUMEROmAGICO);
  writeln;
  
  // Exemplo com cores
  cor := $3498DB;  // Uma cor azulada
  writeln('Cor em decimal: ', cor);
  ExtrairComponentesRGB(cor);
  writeln;
  
  // Exemplo com flags
  flags := FLAGaTIVO or FLAGeDITAVEL;  // Ativo e editável
  writeln('Flags: ', flags);
  VerificarFlags(flags);
  writeln;
  
  // Operações com hexadecimal
  valor := $A;
  writeln('Valor inicial: ', valor);
  valor := valor shl 4;  // Deslocamento para esquerda (equivalente a multiplicar por 16)
  writeln('Após deslocamento: ', valor, ' (0x', hexStr(valor, 8), ')');
  
  writeln;
  writeln('Pressione ENTER para sair...');
  readln;
end.