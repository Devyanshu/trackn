package com.example.tracknt;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class griev extends AppCompatActivity {
    private EditText multi;
    private Button btn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_griev);
        multi = (EditText)findViewById(R.id.editText6);
        btn  = (Button)findViewById(R.id.button5);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                FirebaseDatabase database = FirebaseDatabase.getInstance();
                DatabaseReference myRef = database.getReference("griev");

                myRef.setValue(multi.getText().toString());
                multi.setText(null);
                Toast.makeText(griev.this, "Complaint sent !",
                        Toast.LENGTH_SHORT).show();
                Intent intent = new Intent(griev.this, general.class);
                startActivity(intent);
            }
        });

    }

}
