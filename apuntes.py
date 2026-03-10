
# Ejemplo de solicitud
curl --location -g '{{Domain}}/v1/messages' \
--header 'API-KEY: API Key' \
--data '{
    "to":"919999999999",
    "recipient_type": "individual",
    "type":"text",
    "text":{
        "body": "Your Message Here"
    }
}'

# JSON
{
    "to":"91999999999",
    "recipient_type": "individual",
    "type":"image",
    "image":{
        "link": "Your Image Link Here"
    }
}

{
    "to":"91999999999",
    "recipient_type": "individual",
    "type":"video",
    "video":{
        "link": "Your Video Link Here"
    }
}

{
    "to":"91999999999",
    "recipient_type": "individual",
    "type":"document",
    "document":{
        "link": "Your document Link Here",
        "filename": "File Name Here"
    }
}

{
  "to": "91999999999",
  "recipient_type": "individual",
  "type": "interactive",
  "interactive": {
    "type": "list",
    "header": {
      "type": "text",
      "text": "your-header-content"
    },
    "body": {
      "text": "your-text-message-content"
    },
    "footer": {
      "text": "your-footer-content"
    },
    "action": {
      "button": "Button Text Comes Here",
      "sections":[
        {
          "title":"your-section-title-content",
          "rows": [
            {
              "id":"unique-row-identifier",
              "title": "row-title-content",
              "description": "row-description-content"          
            },
            {
              "id":"unique-row-identifier",
              "title": "row-title-content",
              "description": "row-description-content"          
            }
          ]
        }
      ]
    }
  }
}

{
  "to": "91999999999",
  "recipient_type": "individual",
  "type": "interactive",
  "interactive": {
    "type": "list",
    "header": {
      "type": "text",
      "text": "your-header-content"
    },
    "body": {
      "text": "your-text-message-content"
    },
    "footer": {
      "text": "your-footer-content"
    },
    "action": {
      "button": "Button Text Comes Here",
      "sections":[
        {
          "title":"your-section-title-content",
          "rows": [
            {
              "id":"unique-row-identifier",
              "title": "row-title-content",
              "description": "row-description-content"          
            }
          ]
        },
        {
          "title":"your-section-title-content",
          "rows": [
            {
              "id":"unique-row-identifier",
              "title": "row-title-content",
              "description": "row-description-content"          
            }
          ]
        }
      ]
    }
  }
}

{
  "to": "91999999999",
  "recipient_type": "individual",
  "type": "interactive",
  "interactive": {
    "type": "button",
    # start header
    "header": {
      "type": "text" | "image" | "video" | "document",
      "text": "your text"

      # OR
      "document": {
        "link": "the-provider-name/protocol://the-url",
        "filename": "some-file-name"
      },

      # OR
      "video": {
        "link": "the-provider-name/protocol://the-url",
      }

      # OR
      "image": {
        "link": "http(s)://the-url",
      }
    }, # end header
    "body": {
      "text": "your-text-body-content"
    },
    "footer": { # optional
      "text": "your-text-footer-content"
    },
    "action": {
      "buttons": [
        {
          "type": "reply",
          "reply": {
            "id": "unique-postback-id",
            "title": "First Button’s Title" 
          }
        },
        {
          "type": "reply",
          "reply": {
            "id": "unique-postback-id",
            "title": "Second Button’s Title" 
          }
        }
      ] 
    }
  }
}

{
    "to": "RECEIVER_NUMBER",
    "recipient_type": "individual",
    "type": "template",
    "template": {
        "language": {
            "policy": "deterministic",
            "code": "en"
        },
        "name": "test",
        "components": []
    }
}

{{Domain}}/v1/configs/templates/template_id

{
    "name":"text_header_template",
    "category":"ALERT_UPDATE",
    "language":"en",
    "components":[
        {
            "type":"HEADER",
            "format":"TEXT",
            "text":"Text Header Can Have Only One Variable {{1}}",
            "example":{
                "header_text":[
                    "headerVariable"
                ]
            }
        },
        {
            "type":"FOOTER",
            "text":"Footer Text"
        },
        {
            "type":"BODY",
            "text":"Hello {{1}}\n\nThis is a test body {{2}}  ",
            "example":{
                "body_text":[
                    [
                        "bodyVariable1",
                        "bodyVariable2"
                    ]
                ]
            }
        },
        {
            "type":"BUTTONS",
            "buttons":[
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 1"
                },
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 2"
                },
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 3"
                }
            ]
        }
    ]
}

{
    "name":"text_header_template",
    "category":"ALERT_UPDATE",
    "language":"en",
    "components":[
        {
            "type":"HEADER",
            "format":"TEXT",
            "text":"Text Header Can Have Only One Variable {{1}}",
            "example":{
                "header_text":[
                    "headerVariable"
                ]
            }
        },
        {
            "type":"FOOTER",
            "text":"Footer Text"
        },
        {
            "type":"BODY",
            "text":"Hello {{1}}\n\nThis is a test body {{2}}  ",
            "example":{
                "body_text":[
                    [
                        "bodyVariable1",
                        "bodyVariable2"
                    ]
                ]
            }
        },
        {
            "type":"BUTTONS",
            "buttons":[
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 1"
                },
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 2"
                },
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 3"
                }
            ]
        }
    ]
}

{
    "name":"no_header_template",
    "category":"ALERT_UPDATE",
    "language":"en",
    "components":[
        {
            "type":"BODY",
            "text":"Hello {{1}}\n\nThis is a test body {{2}} ",
            "example":{
                "body_text":[
                    [
                        "bodyVariable1",
                        "bodyVariable2"
                    ]
                ]
            }
        }
    ]
}

{
    "name":"text_header_template",
    "category":"ALERT_UPDATE",
    "language":"en",
    "components":[
        {
            "type":"HEADER",
            "format":"TEXT",
            "text":"Text Header Can Have Only One Variable {{1}}",
            "example":{
                "header_text":[
                    "headerVariable"
                ]
            }
        },
        {
            "type":"FOOTER",
            "text":"Footer Text"
        },
        {
            "type":"BODY",
            "text":"Hello {{1}}\n\nThis is a test body {{2}}  ",
            "example":{
                "body_text":[
                    [
                        "bodyVariable1",
                        "bodyVariable2"
                    ]
                ]
            }
        },
        {
            "type":"BUTTONS",
            "buttons":[
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 1"
                },
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 2"
                },
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 3"
                }
            ]
        }
    ]
}

{
    "name":"image_header_template",
    "category":"ALERT_UPDATE",
    "language":"en",
    "components":[
        {
            "type":"HEADER",
            "format":"IMAGE",
            "example":{
                "header_handle":[
                    "https://confidentialcontent.s3.eu-west-1.wasabisys.com/waba/l4y50apq.jpeg"
                ]
            }
        },
        {
            "type":"FOOTER",
            "text":"Footer Text"
        },
        {
            "type":"BODY",
            "text":"Hello {{1}}\n\nThis is a test body {{2}} ",
            "example":{
                "body_text":[
                    [
                        "bodyVariable1",
                        "bodyVariable2"
                    ]
                ]
            }
        },
        {
            "type":"BUTTONS",
            "buttons":[
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 1"
                },
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 2"
                },
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 3"
                }
            ]
        }
    ]
}

{
    "name":"image_header_template",
    "category":"ALERT_UPDATE",
    "language":"en",
    "components":[
        {
            "type":"HEADER",
            "format":"DOCUMENT",
            "example":{
                "header_handle":[
                    "https://confidentialcontent.s3.eu-west-1.wasabisys.com/waba/l2rlatc4.pdf"
                ]
            }
        },
        {
            "type":"FOOTER",
            "text":"Footer Text"
        },
        {
            "type":"BODY",
            "text":"Hello {{1}}\n\nThis is a test body {{2}} ",
            "example":{
                "body_text":[
                    [
                        "bodyVariable1",
                        "bodyVariable2"
                    ]
                ]
            }
        },
        {
            "type":"BUTTONS",
            "buttons":[
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 1"
                },
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 2"
                },
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 3"
                }
            ]
        }
    ]
}

{
    "name":"image_header_template",
    "category":"ALERT_UPDATE",
    "language":"en",
    "components":[
        {
            "type":"HEADER",
            "format":"VIDEO",
            "example":{
                "header_handle":[
                    "https://confidentialcontent.s3.eu-west-1.wasabisys.com/waba/l4we1qri.mp4"
                ]
            }
        },
        {
            "type":"FOOTER",
            "text":"Footer Text"
        },
        {
            "type":"BODY",
            "text":"Hello {{1}}\n\nThis is a test body {{2}} ",
            "example":{
                "body_text":[
                    [
                        "bodyVariable1",
                        "bodyVariable2"
                    ]
                ]
            }
        },
        {
            "type":"BUTTONS",
            "buttons":[
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 1"
                },
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 2"
                },
                {
                    "type":"QUICK_REPLY",
                    "text":"Button 3"
                }
            ]
        }
    ]
}

# CORREO Establecer webhook
# json

{
  "url": "https://example.com"
}

# borrar eliminar webhook
{{Domain}}/v1/configs/webhook