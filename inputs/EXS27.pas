program valores_mistos;
{ Programa com 4 valores float, 3 valores octais e 3 inteiros }

uses crt;

const
  // Valores float
  PI_VAL          = 3.14159265;
  EULER_VAL       = 2.71828182;
  GRAVITY         = 9.80665;
  GOLDEN_RATIO    = 1.61803398;

  // Valores octais (prefixo 0)
  FILE_PERMISSION = 0755;    // Permissões de arquivo Unix
  MASK_OPTIONS    = 0644;    // Máscara de opções
  USER_GROUP      = 0770;    // Grupo de usuários

  // Valores inteiros
  MAX_USERS       = 100;
  TIMEOUT         = 30;
  BUFFER_SIZE     = 1024;

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
  writeln('4. Razão Áurea....: ', GOLDEN_RATIO:0:8);
  
  writeln;
  writeln('Valores Octais:');
  writeln('---------------');
  writeln('5. Permissões de Arquivo: ', FILE_PERMISSION);
  writeln('6. Máscara de Opções....: ', MASK_OPTIONS);
  writeln('7. Grupo de Usuários....: ', USER_GROUP);
  
  writeln;
  writeln('Valores Inteiros:');
  writeln('-----------------');
  writeln('8. Máximo de Usuários..: ', MAX_USERS);
  writeln('9. Tempo de Espera......: ', TIMEOUT);
  writeln('10. Tamanho do Buffer...: ', BUFFER_SIZE);
  
  writeln;
  writeln('Operações com Octais:');
  writeln('---------------------');
  writeln('FILE_PERMISSION AND 0750 = ', FILE_PERMISSION and 0750);
  writeln('USER_GROUP OR 0007 = ', USER_GROUP or 0007);
  
  writeln;
  writeln('Pressione ENTER para sair...');
  readln;
end.