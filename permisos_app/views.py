from django.shortcuts import render
from django.db import connection
from django.contrib import messages

def verificar_permiso(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        nombre_objeto = request.POST.get('nombre_objeto')
        nombre_permiso = request.POST.get('nombre_permiso')        

 
        if not all([usuario_id, nombre_objeto, nombre_permiso]):
           messages.error(request, "")
           return render(request, 'permisos_app/verificar_permiso.html',{
            'error':"Los campos Usuario ID, Nombre Objeto y Nombre Permiso son obligatorios."
           })
           

        try:
            with connection.cursor() as cursor:            
                cursor.execute(
                    'EXEC dbo.VerificarPermisoUsuario %s, %s, %s',
                    [
                        int(usuario_id),  
                        nombre_objeto,
                        nombre_permiso,                        
                    ]
                )
                resultado = cursor.fetchone()
                tiene_permiso = resultado[0] if resultado else False                

            return render(request, 'permisos_app/resultado_permiso.html', {
                'tiene_permiso': tiene_permiso,
                
            })

        except Exception as e:
            messages.error(request, f"Error al verificar el permiso: {str(e)}")            
            print(f"Error en verificar_permiso: {e}")
            
    return render(request, 'permisos_app/verificar_permiso.html')