Function showmenu {
    Clear-Host
    Write-Host "Iniciando Menu..."
    Write-Host "1. Ver estatus de perfil"
    Write-Host "2. Cambiar estatus de perfil"
    Write-Host "3. Ver perfil de red actual"
    Write-Host "4. Cambiar perfil de red actual"
    Write-Host "5. Ver reglas de bloqueo"
    Write-Host "6. Agregar reglas de bloqueo"
    Write-Host "7. Eliminar reglas de bloqueo"
    Write-Host "8. Salir"
}
 
showmenu
 
while(($inp = Read-Host -Prompt "Selecciona una opcion") -ne "8"){
 
switch($inp){
        1 {
            Clear-Host
            Ver-StatusPerfil
            pause;
            break 
         }

        2{
            Clear-Host
            Cambiar-StatusPerfil
            pause;
            break  
         }

        3{
            Clear-Host
            Ver-PerfilRedActual
            pause;
            break  
         }

        4{
            Clear-Host
            Cambiar-PerfilRedActual
            pause;
            break
         } 

        5 {
            Clear-Host
            Ver-ReglasBloqueo
            pause;
            break 
         }

        6 {
            Clear-Host
            Agregar-ReglasBloqueo
            pause;
            break 
         }

        7 {
            Clear-Host
            Eliminar-ReglasBloqueo
            pause;
            break 
           }
           
        8 {"Salir"; break}
        default {Write-Host -ForegroundColor red -BackgroundColor white "Opcion invalida. Favor de seleccionar otra opcion";pause}
        
    }

showmenu
}