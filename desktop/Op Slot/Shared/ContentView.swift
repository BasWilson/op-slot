//
//  ContentView.swift
//  Shared
//
//  Created by Bas Wilson on 27/11/2020.
//

import SwiftUI


struct ContentView: View {

    var body: some View {
        NavigationView {
            List {
                Text("Op slot")
                Group{
                    NavigationLink(destination: PasswordsListView()) {
                        Label("Passwords", systemImage: "lock")
                    }
     
                }
                Text("Misc")
                Group{
                    NavigationLink(destination: ContentView()) {
                        Label("Account", systemImage: "person")
                    }
                    
                    NavigationLink(destination: ContentView()) {
                        Label("Settings", systemImage: "gear")
                    }
                }
            }
            
        }
    }
}

struct PasswordsListView: View {
    @State private var showingAlert = false

    var body: some View {
        NavigationView {
            List{
                NavigationLink(
                    destination: VStack{
                        
                        HStack{
                            Label("wilson@metinspace.com", systemImage: "envelope.fill")
                            Button(action: {}) {
                                Text("Copy email")
                            }
                        }
                        
                        HStack{
                            Label("************", systemImage: "lock.fill")
                            Button(action: {}) {
                                Text("Copy password")
                            }
                        }
                        
                        Button(action: {
                            self.showingAlert = true
                        }) {
                            Text("Delete")
                        }.accentColor(.red).padding(20)

                    },
                    label: {
                        Text("hvh.gg")
                    })
            }
        }.alert(isPresented: $showingAlert) {
            
            Alert(title: Text("Are you sure you want to delete this password for"), message: Text("hvh.gg"), primaryButton: .default(Text("No")), secondaryButton: .default(Text("Yes")))
            
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        PasswordsListView()
    }
}
