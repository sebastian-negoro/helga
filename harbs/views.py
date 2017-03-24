import os, json, time
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render
from django.core.files import File
from .models import HockeyMatch, HockeyTeam
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

def index(request):
	hockey_matches = HockeyMatch.objects.all()
		
	#open_match("https://www.marathonbet.com/en/live/43658")

	context = { 'hockey_matches': hockey_matches }
	return render (request, 'harbs/index.html', context)

def match_list(request):
	driver_match_list = webdriver.Firefox()
	driver_match_list.get("https://www.marathonbettinres.com/en/live/popular")

	match_list_path = os.path.join(settings.BASE_DIR, 'harbs/static/harbs/js/match_list.js')
	with open(match_list_path, 'r') as match_list_js:
		match_list = match_list_js.read()
		driver_match_list.execute_script(match_list)

	return HttpResponse('')

def generate_page(request):

	# FIREFOX WITH ZENMATE AND RANDOM AGENT SPOOFER
	profile = webdriver.FirefoxProfile()

	zenmate_path = os.path.join(settings.BASE_DIR, 'harbs/static/harbs/js/zenmate-firefox.xpi')
	profile.add_extension(zenmate_path)
	profile.set_preference("ZenMate", "4.1.2")

	ras_path = os.path.join(settings.BASE_DIR, 'harbs/static/harbs/js/random_agent_spoofer-0.9.5.6-fx.xpi')
	profile.add_extension(ras_path)
	profile.set_preference("Random Agent Spoofer", '0.9.5.6')

	driver = webdriver.Firefox(profile)
	driver.get()

	return HttpResponse('')

def send_coefs_ajax(request):
	if request.method == 'GET':
		coefs = request.GET.get('json_coefs')
		print(coefs)
		#request.session['coefs'] = coefs
		#print(request.session['coefs'])

		return HttpResponse('')

def open_match(request):
	match_link = request.GET.get('match_link')


	#profile = webdriver.FirefoxProfile()
	#profile.accept_untrusted_certs = True
	#capabilities = DesiredCapabilities.FIREFOX.copy()
	#capabilities.update({'acceptInsecureCerts': True})
	#driver_marathon = webdriver.Firefox(capabilities = capabilities)

	#dcap = dict(DesiredCapabilities.PHANTOMJS)
	#dcap["phantomjs.cli.args"] = ("--ignore-ssl-errors=true --web-security=false")
	#driver_marathon = webdriver.PhantomJS(desired_capabilities=dcap)
	#driver_marathon = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any', '--web-security=false'], desired_capabilities={'acceptSslCerts': 'true'})

	#service_args = [
	#	'--debug=true',
	#	'--web-security=no',
	#]
	#driver_marathon = webdriver.PhantomJS(service_args=service_args)

	chrome_options = Options()
	chrome_options.add_argument("--disable-web-security")
	chrome_options.add_argument("--user-data-dir=")
	driver_marathon = webdriver.Chrome(chrome_options=chrome_options)

	driver_marathon.get(match_link)
	#time.sleep(5)
	#driver_marathon.save_screenshot('screen.jpg')
	#for entry in driver_marathon.get_log('browser'):
		#print(entry)
	
	jquery_path = os.path.join(settings.BASE_DIR, 'harbs/static/harbs/js/jquery-3.1.1.min.js')
	with open(jquery_path, 'r') as jquery_js:
		jquery = jquery_js.read()
		driver_marathon.execute_script(jquery)

	marathon_bets_path = os.path.join(settings.BASE_DIR, 'harbs/static/harbs/js/marathon_bets.js')
	with open(marathon_bets_path, 'r') as marathon_bets_js:
		marathon_bets = marathon_bets_js.read()
		driver_marathon.execute_script(marathon_bets)

	return HttpResponse('')
	
# Create your views here.
