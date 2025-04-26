program ConstantesHexadecimais;

const
  // Constantes em hexadecimal
  MASCARA_VERMELHA := 0xFF0000;     
  MASCARA_VERDE    := 0x00FF00;     
  MASCARA_AZUL     := 0x0000FF;     
  FLAG_ATIVO       := 0x01;         
  FLAG_VISIVEL     := 0x02;         
  FLAG_EDITAVEL    := 0x04;         
  NUMERO_MAGICO    := 0xDEADBEEF;

var
  cor: integer;
  flags: byte;
  valor: cardinal;

// Função para extrair componentes de cor RGB
procedure ExtrairComponentesRGB(cor: integer);
var
  vermelho, verde, azul: byte;
begin
  vermelho := (cor and MASCARA_VERMELHA) shr 16;
  verde := (cor and MASCARA_VERDE) shr 8;
  azul := cor and MASCARA_AZUL;
  
  writeln('Componentes RGB:');
  writeln('Vermelho: ', vermelho);
  writeln('Verde:    ', verde);
  writeln('Azul:     ', azul);
end;

// Função para verificar flags
procedure VerificarFlags(flags: byte);
begin
  writeln('Status:');
  writeln('Ativo:    ', (flags and FLAG_ATIVO) <> 0);
  writeln('Visível:  ', (flags and FLAG_VISIVEL) <> 0);
  writeln('Editável: ', (flags and FLAG_EDITAVEL) <> 0);
end;

begin
  writeln('Número mágico: ', NUMERO_MAGICO);
  writeln;
  
  // Exemplo com cores
  cor := $3498DB;  // Uma cor azulada
  writeln('Cor em decimal: ', cor);
  ExtrairComponentesRGB(cor);
  writeln;
  
  // Exemplo com flags
  flags := FLAG_ATIVO or FLAG_EDITAVEL;  // Ativo e editável
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