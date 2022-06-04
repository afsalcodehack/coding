package main

import (
	"context"
	"encoding/json"
	"fmt"
	"go_start/model"
	service "go_start/userservice"
	"log"
	"net/http"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

func homePage(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Welcome to the HomePage!")
	fmt.Println("Endpoint Hit: homePage")
}

func returnAllArticles(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Endpoint Hit: returnAllArticles")
	json.NewEncoder(w).Encode(Articles)
}

func getAllDatabases(w http.ResponseWriter, r *http.Request) {
	client, err := mongo.NewClient(options.Client().ApplyURI("mongodb://localhost:27017"))
	if err != nil {
		log.Fatal(err)
	}
	ctx, _ := context.WithTimeout(context.Background(), 10*time.Second)
	err = client.Connect(ctx)
	if err != nil {
		log.Fatal(err)
	}
	defer client.Disconnect(ctx)

	/*
	   List databases
	*/
	//databases, err := client.ListDatabaseNames(ctx, bson.M{})
	if err != nil {
		log.Fatal(err)
	}

	collection := client.Database("hr").Collection("employee")

	filter := bson.D{{"bedrooms", bson.D{{"$lt", 3}}}, {"accommodates", bson.D{{"$gt", 7}}}}
	//filter := bson.D{{"name", "Ribeira Charming Duplex"}}
	project := bson.D{{"name", 1}}
	opts := options.Find().SetProjection(project)

	cursor, err := collection.Find(context.TODO(), filter, opts)
	if err != nil {
		log.Fatal(err)
	}
	var episodes []bson.M
	if err = cursor.All(ctx, &episodes); err != nil {
		log.Fatal(err)
	}
	fmt.Println(episodes)

	print(collection)
	json.NewEncoder(w).Encode(episodes)
}

func handleRequests() {

	http.HandleFunc("/", homePage)
	http.HandleFunc("/data", returnAllArticles)
	http.HandleFunc("/db", getAllDatabases)
	log.Fatal(http.ListenAndServe(":8081", nil))
}

var Articles []model.Article

func main() {
	fmt.Println(getCustomer())
	fmt.Println(service.GetService())
	Articles = []model.Article{
		{Title: "Helloss", Desc: "Article Descriptions", Content: "some content"},
		{Title: "Hello 2cc", Desc: "Article Description", Content: "Article Content"},
	}
	fmt.Print("Connection Started..", Articles)
	handleRequests()
}
