package main

import (
	"encoding/json"
	"fmt"
	"go_start/model"
	service "go_start/userservice"
	"log"
	"net/http"
)

func homePage(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Welcome to the HomePage!")
	fmt.Println("Endpoint Hit: homePage")
}

func returnAllArticles(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Endpoint Hit: returnAllArticles")
	json.NewEncoder(w).Encode(Articles)
}

func handleRequests() {

	http.HandleFunc("/", homePage)
	http.HandleFunc("/data", returnAllArticles)
	log.Fatal(http.ListenAndServe(":8081", nil))
}

var Articles []model.Article

func main() {
	fmt.Println(getCustomer())
	fmt.Println(service.GetService())
	Articles = []model.Article{
		{Title: "Hello", Desc: "Article Description", Content: "some content"},
		{Title: "Hello 2cc", Desc: "Article Description", Content: "Article Content"},
	}
	fmt.Print("Connection Started..", Articles)
	handleRequests()
}
