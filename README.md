1. Test setup:
	- Tests are written in python 2.7, 
	- I don't know cucumber/ruby framework so I wanted to experiment with selenium + python
	- I'm using selenium 3
	- ./config.json is a config file defining browser and tested page url
	- test are grouped by header menu option and executed in suite
	
2. Organization
	- I wanted to imitate BDD approach presented in cucumber/ruby so I created steps: given, and, then
	- Thanks of that tests are cleaner and easier to read
	- I'm using page object pattern design pattern: locators were separated, I created objects for significant elements on a page/ or page itself. So it means that 
      you can see object for header menu, side menu and of course object like login page. 

3. Features
	- I wanted to find features possible to test without login. This is a production environment and I didn't want to push any unnecessary data.
	- I choose: RSS page and Shop page.
	- My first test "test_user_can_not_add_new_feed_unless_login" consists of following steps: user navigates to RSS page, he tries to add new feed but He is 
	  redirected to login page
	- Second test "test_user_can_browse_list_of_top_feeds" consists of following steps: user navigates to top feeds/syndicated feeds page, browse feeds, and
	  come back to RSS page
	- Third test "test_user_cannot_upgrade_to_paid_account_unless_login" check that user cannot upgrade account, click button add to card if he is not logged in
	
	
4. How to run tests locally
	- install python 2.7
	- download pip
	- install selenium
	- download drivers geckodriver version , firefox and chrome driver,
	- set update path env variable with driver location
	- to run test suite from command line in windows 
		: run cmd
		: enter script/ suite folder:  cd [path]\GalezaLiveJournal\test_suite
		: export project location to pythonpath:  set PYTHONPATH=[path]\GalezaLiveJournal 
		: execute suit: python test_suite.py