
| BlobType | Description |
| --- | --- |
| 0 | Downtime Image |
| 1 | Equipment Image |


`id` = the ID of our breadcrumb in the subscriptions (or downtime event id)

# Inserting the image
1. Query to insert image for a thing {type: "Equipment Image", "imageId": 1234, "blob": `blob data`}
	2. Return the uuid of the inserted image
2. If there is already an image for the thing, delete that one, and then insert the new one
| uuid      | BlobType | id   | blob        |
| ---       | ---      | ---  | ---         |
| 123456789 | 1        | 1234 | `blob data` |

# Getting the image
1. If its an equipment image, query for the uuid of the image
```
SELECT [uuid] FROM [dbo].[EquipmentImage] WHERE [id] = 1234 AND [blobType] = 1
```
1. Request the image from webdev at `/system/webdev/DanPT/images/123456789`



