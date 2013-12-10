package main

import (
  "github.com/amir/raidman"
  "os"
  "fmt"
  "strconv"
)

func main() {

  if len(os.Args) != 7 {
    fmt.Printf("usage: %s <host> <service> <state> <description> <ttl> <server:port>\n\n", os.Args[0])
    panic("wrong number of arguments")
  }

  c, err := raidman.Dial("tcp", os.Args[6])
  if err != nil {
    panic(err)
  }

  f, err := strconv.ParseFloat(os.Args[5], 32)
  if err != nil {
    panic(err)
  }

  var state string

  switch os.Args[3] {
    case "0": state = "ok"
    case "1": state = "warning"
    case "2": state = "critical"
    case "3": state = "unknown"
    default : state = os.Args[3]
  }

  var event = &raidman.Event{
    Host:         os.Args[1],
    Service:      os.Args[2],
    State:        state,
    Description:  os.Args[4],
    Ttl:          float32(f),
    Tags:         []string{"nagios"},
  }

  err = c.Send(event)
  if err != nil {
    panic(err)
  }

  c.Close()
}
