const PROPERTIES = (
  "Dish Type",
  "Source Site",
  "Serves"
)

export function createPagePostBody(recipeResponse) {
  let pageBody = {}

    pageBody.parent = {
      "type": "database_id",
      "database_id": process.env.DATABASE_ID
    }

    pageBody.cover = recipeResponse.image ? {
      "type": "external",
      "external": {
        "url": recipeResponse.image
      }
    } : null
    
    pageBody.properties = generateProperties(recipeResponse)

    return pageBody
}


function generateProperties(recipeResponse) {
  return {
    "Name": {
      "title": [
        {
          "text": {
            "content": recipeResponse.title
          }
        }
      ]
    },
    "Dish Type": {
      "multi_select": [{
        "name": recipeResponse.category
      }]
      
    }, 
    "Source Site": {
      "url": recipeResponse.canonical_url
    },
    "Serves": {
      rich_text: [{
        "type": "text",
        "text": {
          "content": recipeResponse.yields,
          "link": null
        },
        "annotations": {
          "bold": false,
          "italic": false,
          "strikethrough": false,
          "underline": false,
          "code": false,
          "color": "default"
        },
        "plain_text": recipeResponse.yields,
        "href": null
      }]
    }
  }
  
}

function generateIngredientsColumn() {}

function generateStepsColumn() {}

function makeContent() {}

function generateRecipeObject(properties, content) {
  // format all information into an object that's ready to be pushed to notion
}