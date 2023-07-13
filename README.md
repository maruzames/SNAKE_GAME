**********
*  PYSTACK WEEK 7.0
*  https://pythonando.com.br/
*  
*  Aula 01 (Sistema Windows11/VSCode/Configurações Iniciais)
**********
Criar Ambiente Virtual.
Instalar Django & Pacotes adicionais.

**********
*  Aula 02a (App Extrato)
**********
Adicionar o app Extrato 

**********
*  Aula 02b
**********
EXportar Extrato

pip install weasyprint

quem usa windows, instalar o arq: 
'https://github.com/tschoonj/gtk-for-windows-runtime-environment-installer/releases'

**********
*  Aula 02c
**********

Definir planejamento

python manage.py startapp planejamento

CORE/settings.py  // ... INSTALLED_APPS = 'planejamento',
CORE/urls.py      // ... path('planejamento/', include('planejamento.urls')),

planejamento/urls.py   // ... path('definir_planejamento/')
planejamento/views.py  // ... def definir_planejamento(request):

planejamento/templates/definir_planejamento.html //.

**********
*  Aula 02d
**********

Ver planejamento 

urls.py() / views.py() & HTML

**********
*  Aula 03
**********
Iniciar o Ambiente Virtual
		venv\Scripts\Activate
		
>>Definir Contas

python manage.py startapp contas

CORE/settings.py  // ... INSTALLED_APPS = 'contas',
CORE/urls.py      // ... path('contas/', include('contas.urls')),

contas/urls.py   // ... path('definir_contas/')
contas/views.py  // ... def definir_contas(request):

contas/templates/definir_contas.html //.

**********
*  Aula 03 - Final
**********

Dashboard