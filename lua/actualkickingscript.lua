local url = "link"
game.Players.PlayerAdded:Connect(function(p)
    while wait() do
        if p.Name == game:GetService("HttpService"):GetAsync(url, true) then
            p:Kick("You have been kicked from this game by a developer")
        end
    end
end)