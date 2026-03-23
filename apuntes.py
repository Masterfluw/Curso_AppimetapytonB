
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



# curl -i -X POST `
  https://graph.facebook.com/v22.0/1016468574875369/messages `
  'Authorization: Bearer EAAXHYImI1ZBEBQxeN4CvZB5QV9PokDC5bHsmFpVfImZCMNe7lc5ZBBAPjsLmruQQqNRcSfT2zcq08gfYSLTXegeOX55fTGpo6D45vH4Ekwki7jPZCVQ09xOkw46ahK8fq4gtTVCuSSO0LjvlNzYBcaKhjKOrMgXs1VYywjofMI2n8gQU2qWC6Thbc9BmlZCKPjN28aLZCx5hpUOd8vdSRCnQvZAifrAtJGZBTQDOCIQzZCejDzGNT6ZCyus4iy3348WItbRY6qX3xhQogF2HHXZB2M2w' `
  'Content-Type: application/json' `
  '{ \"messaging_product\": \"whatsapp\", \"to\": \"51941964894\", \"type\": \"template\", \"template\": { \"name\": \"hello_world\", \"language\": { \"code\": \"en_US\" } } }'

# ruta del proyecto git hub

https://github.com/Masterfluw/Curso_appimetapytonb.git
# repositorio  or create a new repository on the command line  --  O crear un nuevo repositorio desde la línea de comandos
 echo "# Curso_appimetapytonb" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Masterfluw/Curso_appimetapytonb.git
git push -u origin main

# or push an existing repository from the command line --  o enviar un repositorio existente desde la línea de comandos
git remote add origin https://github.com/Masterfluw/Curso_appimetapytonc.git
git branch -M main
git push -u origin main

# webhook
{
    "object":"whatsapp_business_account",
    "entry":[
    {
        "id":"102290129340398",
        "changes":[
        {
        "value":{ 
        "messaging_product":"whatsapp",
        "metadata":{
            "display_phone_number":"15550783881",
            "phone_number_id":"106540352242922"
            },
            "contacts":[
                {
                    "profile":{
                        "name":"Sheena Nelson"
                        },
                        "wa_id":"16505551234"
                        }
                        ],
                        "messages":[
                            {
                                "from":"16505551234",
                                "id""wamid.HBgLMTY1MDM4Nzk0MzkVAgASGBQzQTRBNjU5OUFFRTAzODEwMTQ0RgA=",
                                "timestamp": "1749416383",
                                "type": "text"
                                "text":{
                                    "body":"Doesitcomeinanothercolor?"
                                    }
                            }
                                    ]
                },
                                    "field":"messages"
        }
            ]
    }
    ]
}
