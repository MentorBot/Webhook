# Webhook
This Webhook Returns a response to the NLP server we will be using for the application.
This Webhook will also be used by the front end to input data into the DB.
The language used to build this API is python, Django and hosted on a heroku server.


### Usage

| URL Endpoint | HTTP Method | Functionality     | Parameter |
|--------------|-------------|-------------------|-----------|
| /mb/search/  | GET         | Search Query      | q=[query] |
| /mb/mentors/ | GET         | Category          |           |
| /na/         | GET         | Displays all data |           |

### Tests

Use nosetests to run tests (with stdout) like this: $ nosetests --nocapture

### Contributing

If you'd like to contribute to HealthTools.API, check out the `CONTRIBUTING.md ` file on how to get started.

### License

MIT License

Copyright (c) 2018 MentorBot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
