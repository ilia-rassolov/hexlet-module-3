{
  "log": {
    "version": "1.2",
    "creator": {
      "name": "WebInspector",
      "version": "537.36"
    },
    "pages": [],
    "entries": [
      {
        "_initiator": {
          "type": "script",
          "stack": {
            "callFrames": [
              {
                "functionName": "",
                "scriptId": "119",
                "url": "https://cdn.carrotquest.app/chunk-tags.js",
                "lineNumber": 185,
                "columnNumber": 27898
              },
              {
                "functionName": "R",
                "scriptId": "119",
                "url": "https://cdn.carrotquest.app/chunk-tags.js",
                "lineNumber": 185,
                "columnNumber": 26839
              },
              {
                "functionName": "d",
                "scriptId": "103",
                "url": "https://cdn.carrotquest.app/index.js",
                "lineNumber": 25,
                "columnNumber": 59082
              },
              {
                "functionName": "Pi.carrotquest.statusTracking.heartBeat",
                "scriptId": "103",
                "url": "https://cdn.carrotquest.app/index.js",
                "lineNumber": 25,
                "columnNumber": 57138
              }
            ]
          }
        },
        "_priority": "High",
        "_resourceType": "xhr",
        "cache": {},
        "connection": "51332",
        "request": {
          "method": "POST",
          "url": "https://api.carrotquest.app/v1/users/$self_user/setpresence",
          "httpVersion": "http/2.0",
          "headers": [
            {
              "name": ":authority",
              "value": "api.carrotquest.app"
            },
            {
              "name": ":method",
              "value": "POST"
            },
            {
              "name": ":path",
              "value": "/v1/users/$self_user/setpresence"
            },
            {
              "name": ":scheme",
              "value": "https"
            },
            {
              "name": "accept",
              "value": "*/*"
            },
            {
              "name": "accept-encoding",
              "value": "gzip, deflate, br, zstd"
            },
            {
              "name": "accept-language",
              "value": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
            },
            {
              "name": "content-length",
              "value": "801"
            },
            {
              "name": "content-type",
              "value": "multipart/form-data; boundary=----WebKitFormBoundaryhemF32MaNDblEho8"
            },
            {
              "name": "origin",
              "value": "https://ru.hexlet.io"
            },
            {
              "name": "priority",
              "value": "u=1, i"
            },
            {
              "name": "sec-ch-ua",
              "value": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\""
            },
            {
              "name": "sec-ch-ua-mobile",
              "value": "?1"
            },
            {
              "name": "sec-ch-ua-platform",
              "value": "\"Android\""
            },
            {
              "name": "sec-fetch-dest",
              "value": "empty"
            },
            {
              "name": "sec-fetch-mode",
              "value": "cors"
            },
            {
              "name": "sec-fetch-site",
              "value": "cross-site"
            },
            {
              "name": "user-agent",
              "value": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36"
            }
          ],
          "queryString": [],
          "cookies": [],
          "headersSize": -1,
          "bodySize": 801,
          "postData": {
            "mimeType": "multipart/form-data; boundary=----WebKitFormBoundaryhemF32MaNDblEho8",
            "text": "------WebKitFormBoundaryhemF32MaNDblEho8\r\nContent-Disposition: form-data; name=\"presence\"\r\n\r\nidle\r\n------WebKitFormBoundaryhemF32MaNDblEho8\r\nContent-Disposition: form-data; name=\"current_page\"\r\n\r\nАрхитектура Веба | Python: Веб-разработка (Flask)\r\n------WebKitFormBoundaryhemF32MaNDblEho8\r\nContent-Disposition: form-data; name=\"current_url\"\r\n\r\nhttps://ru.hexlet.io/courses/python-flask/lessons/web-architecture/theory_unit\r\n------WebKitFormBoundaryhemF32MaNDblEho8\r\nContent-Disposition: form-data; name=\"auth_token\"\r\n\r\nuser.1798411821477005146.64033-37649a1dcf0c27a7d9f778d49b.bf1a33f5669fe5af5a65d588881b49cd0ec84c997462ea3b\r\n------WebKitFormBoundaryhemF32MaNDblEho8\r\nContent-Disposition: form-data; name=\"id_as_string\"\r\n\r\ntrue\r\n------WebKitFormBoundaryhemF32MaNDblEho8--\r\n",
            "params": [
              {
                "name": "presence",
                "value": "idle"
              },
              {
                "name": "current_page",
                "value": "Архитектура Веба | Python: Веб-разработка (Flask)"
              },
              {
                "name": "current_url",
                "value": "https://ru.hexlet.io/courses/python-flask/lessons/web-architecture/theory_unit"
              },
              {
                "name": "auth_token",
                "value": "user.1798411821477005146.64033-37649a1dcf0c27a7d9f778d49b.bf1a33f5669fe5af5a65d588881b49cd0ec84c997462ea3b"
              },
              {
                "name": "id_as_string",
                "value": "true"
              }
            ]
          }
        },
        "response": {
          "status": 200,
          "statusText": "",
          "httpVersion": "http/2.0",
          "headers": [
            {
              "name": "access-control-allow-credentials",
              "value": "true"
            },
            {
              "name": "access-control-allow-origin",
              "value": "https://ru.hexlet.io"
            },
            {
              "name": "allow",
              "value": "OPTIONS, POST"
            },
            {
              "name": "content-length",
              "value": "37"
            },
            {
              "name": "content-type",
              "value": "application/json"
            },
            {
              "name": "date",
              "value": "Fri, 15 Nov 2024 10:43:54 GMT"
            },
            {
              "name": "server",
              "value": "nginx"
            },
            {
              "name": "vary",
              "value": "origin"
            },
            {
              "name": "x-myheader",
              "value": "1"
            }
          ],
          "cookies": [],
          "content": {
            "size": 37,
            "mimeType": "application/json",
            "text": "{\"meta\": {\"status\": 200}, \"data\": {}}"
          },
          "redirectURL": "",
          "headersSize": -1,
          "bodySize": -1,
          "_transferSize": 211,
          "_error": null,
          "_fetchedViaServiceWorker": false
        },
        "serverIPAddress": "95.213.158.106",
        "startedDateTime": "2024-11-15T10:46:43.282Z",
        "time": 45.277000001078704,
        "timings": {
          "blocked": 2.3150000003465685,
          "dns": -1,
          "ssl": -1,
          "connect": -1,
          "send": 0.5850000000000001,
          "wait": 40.821999999996976,
          "receive": 1.5550000007351628,
          "_blocked_queueing": 1.8440000003465684,
          "_workerStart": -1,
          "_workerReady": -1,
          "_workerFetchStart": -1,
          "_workerRespondWithSettled": -1
        }
      },
      {
        "_initiator": {
          "type": "script",
          "stack": {
            "callFrames": [
              {
                "functionName": "",
                "scriptId": "119",
                "url": "https://cdn.carrotquest.app/chunk-tags.js",
                "lineNumber": 185,
                "columnNumber": 27898
              },
              {
                "functionName": "R",
                "scriptId": "119",
                "url": "https://cdn.carrotquest.app/chunk-tags.js",
                "lineNumber": 185,
                "columnNumber": 26839
              },
              {
                "functionName": "d",
                "scriptId": "103",
                "url": "https://cdn.carrotquest.app/index.js",
                "lineNumber": 25,
                "columnNumber": 59082
              },
              {
                "functionName": "Pi.carrotquest.statusTracking.heartBeat",
                "scriptId": "103",
                "url": "https://cdn.carrotquest.app/index.js",
                "lineNumber": 25,
                "columnNumber": 57138
              }
            ]
          }
        },
        "_priority": "High",
        "_resourceType": "xhr",
        "cache": {},
        "connection": "51332",
        "request": {
          "method": "POST",
          "url": "https://api.carrotquest.app/v1/users/$self_user/setpresence",
          "httpVersion": "http/2.0",
          "headers": [
            {
              "name": ":authority",
              "value": "api.carrotquest.app"
            },
            {
              "name": ":method",
              "value": "POST"
            },
            {
              "name": ":path",
              "value": "/v1/users/$self_user/setpresence"
            },
            {
              "name": ":scheme",
              "value": "https"
            },
            {
              "name": "accept",
              "value": "*/*"
            },
            {
              "name": "accept-encoding",
              "value": "gzip, deflate, br, zstd"
            },
            {
              "name": "accept-language",
              "value": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
            },
            {
              "name": "content-length",
              "value": "801"
            },
            {
              "name": "content-type",
              "value": "multipart/form-data; boundary=----WebKitFormBoundaryKwiU3q5C72ntEzWN"
            },
            {
              "name": "origin",
              "value": "https://ru.hexlet.io"
            },
            {
              "name": "priority",
              "value": "u=1, i"
            },
            {
              "name": "sec-ch-ua",
              "value": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\""
            },
            {
              "name": "sec-ch-ua-mobile",
              "value": "?1"
            },
            {
              "name": "sec-ch-ua-platform",
              "value": "\"Android\""
            },
            {
              "name": "sec-fetch-dest",
              "value": "empty"
            },
            {
              "name": "sec-fetch-mode",
              "value": "cors"
            },
            {
              "name": "sec-fetch-site",
              "value": "cross-site"
            },
            {
              "name": "user-agent",
              "value": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36"
            }
          ],
          "queryString": [],
          "cookies": [],
          "headersSize": -1,
          "bodySize": 801,
          "postData": {
            "mimeType": "multipart/form-data; boundary=----WebKitFormBoundaryKwiU3q5C72ntEzWN",
            "text": "------WebKitFormBoundaryKwiU3q5C72ntEzWN\r\nContent-Disposition: form-data; name=\"presence\"\r\n\r\nidle\r\n------WebKitFormBoundaryKwiU3q5C72ntEzWN\r\nContent-Disposition: form-data; name=\"current_page\"\r\n\r\nАрхитектура Веба | Python: Веб-разработка (Flask)\r\n------WebKitFormBoundaryKwiU3q5C72ntEzWN\r\nContent-Disposition: form-data; name=\"current_url\"\r\n\r\nhttps://ru.hexlet.io/courses/python-flask/lessons/web-architecture/theory_unit\r\n------WebKitFormBoundaryKwiU3q5C72ntEzWN\r\nContent-Disposition: form-data; name=\"auth_token\"\r\n\r\nuser.1798411821477005146.64033-37649a1dcf0c27a7d9f778d49b.bf1a33f5669fe5af5a65d588881b49cd0ec84c997462ea3b\r\n------WebKitFormBoundaryKwiU3q5C72ntEzWN\r\nContent-Disposition: form-data; name=\"id_as_string\"\r\n\r\ntrue\r\n------WebKitFormBoundaryKwiU3q5C72ntEzWN--\r\n",
            "params": [
              {
                "name": "presence",
                "value": "idle"
              },
              {
                "name": "current_page",
                "value": "Архитектура Веба | Python: Веб-разработка (Flask)"
              },
              {
                "name": "current_url",
                "value": "https://ru.hexlet.io/courses/python-flask/lessons/web-architecture/theory_unit"
              },
              {
                "name": "auth_token",
                "value": "user.1798411821477005146.64033-37649a1dcf0c27a7d9f778d49b.bf1a33f5669fe5af5a65d588881b49cd0ec84c997462ea3b"
              },
              {
                "name": "id_as_string",
                "value": "true"
              }
            ]
          }
        },
        "response": {
          "status": 200,
          "statusText": "",
          "httpVersion": "http/2.0",
          "headers": [
            {
              "name": "access-control-allow-credentials",
              "value": "true"
            },
            {
              "name": "access-control-allow-origin",
              "value": "https://ru.hexlet.io"
            },
            {
              "name": "allow",
              "value": "POST, OPTIONS"
            },
            {
              "name": "content-length",
              "value": "37"
            },
            {
              "name": "content-type",
              "value": "application/json"
            },
            {
              "name": "date",
              "value": "Fri, 15 Nov 2024 10:45:24 GMT"
            },
            {
              "name": "server",
              "value": "nginx"
            },
            {
              "name": "vary",
              "value": "origin"
            },
            {
              "name": "x-myheader",
              "value": "1"
            }
          ],
          "cookies": [],
          "content": {
            "size": 37,
            "mimeType": "application/json",
            "text": "{\"meta\": {\"status\": 200}, \"data\": {}}"
          },
          "redirectURL": "",
          "headersSize": -1,
          "bodySize": -1,
          "_transferSize": 211,
          "_error": null,
          "_fetchedViaServiceWorker": false
        },
        "serverIPAddress": "95.213.158.106",
        "startedDateTime": "2024-11-15T10:48:13.281Z",
        "time": 47.43600000074366,
        "timings": {
          "blocked": 5.443000001069275,
          "dns": -1,
          "ssl": -1,
          "connect": -1,
          "send": 0.30300000000000005,
          "wait": 40.21000000068254,
          "receive": 1.4799999989918433,
          "_blocked_queueing": 5.070000001069275,
          "_workerStart": -1,
          "_workerReady": -1,
          "_workerFetchStart": -1,
          "_workerRespondWithSettled": -1
        }
      }
    ]
  }
}