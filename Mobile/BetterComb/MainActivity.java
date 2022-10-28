package com.example.combustivel;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;

import com.google.android.material.textfield.TextInputEditText;

public class MainActivity extends AppCompatActivity {

    private ImageView imgGasolina, imgEtanol;
    private Button btnCalcular;
    private TextInputEditText edtGasolina, edtEtanol;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnCalcular = findViewById(R.id.btnCalcular);
        edtEtanol = findViewById(R.id.edtEtanol);
        edtGasolina = findViewById(R.id.edtGasolina);
        imgEtanol = findViewById(R.id.imgEtanol);
        imgGasolina = findViewById(R.id.imgGasolina);
        btnCalcular.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                double Gas = Double.parseDouble(edtGasolina.getText().toString());
                double Eta = Double.parseDouble(edtEtanol.getText().toString());
                boolean Resultado = (Eta <= Gas * 0.7);
                imgEtanol.setVisibility(View.INVISIBLE);
                imgGasolina.setVisibility(View.INVISIBLE);

                if (Resultado){
                    imgEtanol.setVisibility(View.VISIBLE);
                } else{
                    imgGasolina.setVisibility(View.VISIBLE);
                }

            }
        });
        }

    }
