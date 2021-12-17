To-do List for the Axyl website

## Front-End
- [x] Split the Sass file into separate modules
- [x] Make a brief "About" page about the distro and the team
- [ ] Migrate the codebase to TypeScript
- [ ] Build a simple repo stats dashboard with TypeScript and Fetch API

## Back-End
- [x] Build the basic back-end with Flask
- [ ] \(!IMPORTANT!) Write tests with PyTest
- [x] Put the static assets/templates into the right folders
- [ ] Set up the configuration stuff w/ `config.py`
  - [ ] Use a secret key
- [ ] Use SQLAlchemy ORM for interacting with the database
- [ ] Build an API for fetching repo stats on the `/api` route

## Deployment
- [ ] Write a Systemd service for the Gunicorn server
- [ ] Use a reverse proxy to deploy to Caddy
