-- this code updates your site code

local url = "url/update" -- self explanitory

local hs = game:GetService("HttpService")

local data = hs:JSONEncode({ content = "banana" }) 

hs:PostAsync(url, data, Enum.HttpContentType.ApplicationJson)
