program valores_mistos;
{ Programa com 8 valores float e 2 valores hexadecimais (formato 0x) }

uses crt;

const
  // Valores float
  PI_VAL          := 3.14159265;
  EULER_VAL       := 2.71828182;
  GRAVITY         := 9.80665;
  LIGHT_SPEED     := 2.99792458e8;
  GOLDEN_RATIO    := 1.61803398;
  AVOGADRO        := 6.02214076e23;
  PLANCK          := 6.62607015e-34;
  ELECTRON_CHARGE := 1.602176634e-19;

  // Valores hexadecimais (formato 0x)
  MASK_FLAGS      := 0xFF00;
  ERROR_CODE      := 0x1A3F;

var
  i: integer; 

begin
  clrscr;
  
  writeln('Demonstração de Valores Mistos');
  writeln('=============================');
  writeln;
  writeln('Valores Float Definidos:');
  writeln('------------------------');
  writeln('1. PI............: ', PI_VAL:0:8);
  writeln('2. Número de Euler: ', EULER_VAL:0:8);
  writeln('3. Gravidade......: ', GRAVITY:0:5);
  writeln('4. Velocidade Luz.: ', LIGHT_SPEED:0:0);
  writeln('5. Razão Áurea....: ', GOLDEN_RATIO:0:8);
  writeln('6. Número Avogadro: ', AVOGADRO:0:0);
  writeln('7. Constante Planck: ', PLANCK:0:10);
  writeln('8. Carga Elétron..: ', ELECTRON_CHARGE:0:10);
  
  writeln;
  writeln('Valores Hexadecimais:');
  writeln('---------------------');
  writeln('9. Máscara de Flags: ', MASK_FLAGS);
  writeln('10. Código de Erro..: ', ERROR_CODE);
  
  writeln;
  writeln('Operações com Hexadecimais:');
  writeln('--------------------------');
  writeln('MASK_FLAGS AND 0x00FF = ', MASK_FLAGS and $00FF);
  writeln('ERROR_CODE OR 0x0100 = ', ERROR_CODE or $0100);
  
  writeln;
  writeln('Pressione ENTER para sair...');
  readln;
end.