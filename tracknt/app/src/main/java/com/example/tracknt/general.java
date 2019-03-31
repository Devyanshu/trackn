package com.example.tracknt;

import android.app.Application;
import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Build;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.NotificationCompat;
import android.support.v4.app.NotificationManagerCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.ChildEventListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.Map;
import android.app.Notification;
import android.support.v4.app.NotificationCompat;
import android.support.v4.app.NotificationManagerCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

import static com.example.tracknt.App.CHANNEL_ID;


public class general extends AppCompatActivity {
    private TextView num, typ;
    private NotificationManagerCompat notificationManager;
    String number, type,flag;
    private  FirebaseAuth mauth;
    private  Button bt1, chck;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_general);
        chck = findViewById(R.id.check);
        chck.setEnabled(false);

        num = findViewById(R.id.textNum);
        typ = findViewById(R.id.texttype);
        notificationManager = NotificationManagerCompat.from(this);
        mauth= FirebaseAuth.getInstance();

        //num.setText(number);
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        DatabaseReference myRef = database.getReference();
        myRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                Map<String, String> mp1 = (Map<String, String>) dataSnapshot.getValue();
                number = mp1.get("number");
                type = mp1.get("type");
                //flag = mp1.get("flag");
                chck.setEnabled(true  );


            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });

        bt1=(Button)findViewById(R.id.signout);


        bt1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                logOut();
            }
        });


    }


    public void sendOnChannel1(View v) {
        String mess, title, heading, body;
        String phone = "8948066001";

        //num.setText(number);
        //typ.setText(type);
        String notH = "\uD83D\uDE1E Your item is not here yet.";

        if(!number.equals(phone)){
            title = null;
            mess = null;
            heading = notH;
            body = null;
        }
        else {


            if (type.equals("Library")) {
                title = "A gentle remninder";
                mess = "Your Book is due, return it as soon as possible";
                heading = "Reminder !!";
                body = "A book that you issue is soon to be overdue, return it as soon as possible. ";
            } else {
                title = "Hey, Your item is waiting";
                title = "Hey, Your item is waiting";
                mess = "Your " + type + " is ready to be collected";
                heading = "  \uD83D\uDE00 \uD83D\uDE00 It's here !!";
                if (type.equals("Courier")) {
                    body = "Your recent order has reached Bennett, collect it from the Courier Office.";
                } else {
                    body = "Your clothes are all clean and dry and ready to be collected from the Laundry Office";
                }
            }



            Notification notification = new NotificationCompat.Builder(this, CHANNEL_ID)
                    .setSmallIcon(R.drawable.user)
                    .setContentTitle(title)
                    .setContentText(mess)
                    .setPriority(NotificationCompat.PRIORITY_HIGH)
                    .setCategory(NotificationCompat.CATEGORY_MESSAGE)
                    .build();
            notificationManager.notify(1, notification);
        }
        num.setText(heading);
        typ.setText(body);
    }

    public void sendToGriev(View view)
    {
        Intent intent = new Intent(general.this, griev.class);
        startActivity(intent);
    }

    private void logOut() {
        mauth.signOut();
        sendToLogin();
    }
    private void sendToLogin() {
        Intent a=new Intent(general.this,MainActivity.class);
        startActivity(a);
    }

}
