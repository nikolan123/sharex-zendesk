# sharex-zendesk 
---

`sharex-zendesk` is a flask image destination server to upload screenshots to a ZenDesk site from the ShareX client. The project was made in [Python](https://www.python.org/), with the [Flask](http://flask.pocoo.org/) microframework.
By default, it is set to upload to `datasupport.nysed.gov`

## Configuration
In server.py, configure `zenurl` and `secret_key` variables to your desired vaules.

## Setting up
1. Meow loudly in front of your computer
2. Set the secret_key under arguments to the value of the secret_key variable in server.py
3. Install all requirements and run script
4. Import sharex-config.sxcu
5. Ready to go!

## License

`sharex-zendesk` is under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0).
