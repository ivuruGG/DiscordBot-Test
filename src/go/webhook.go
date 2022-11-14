package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
)

type Discord struct {
	Username  string `json:"username"`
	AvatarUrl string `json:"avatar_url"`
	Content   string `json:"content"`
}

func main() {
	var discord Discord
	discord.Username = "Mr. Hogehoge"
	discord.AvatarUrl = "https://github.com/qiita.png"
	discord.Content = "Hello World!"

	// encode json
	discord_json, _ := json.Marshal(discord)
	fmt.Println(string(discord_json))

	// discord webhook_url
	webhook_url := "取得したURL"
	res, _ := http.Post(
		webhook_url,
		"application/json",
		bytes.NewBuffer(discord_json),
	)
	defer res.Body.Close()
}
