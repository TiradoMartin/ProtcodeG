  private async void Validate()
        {
            SALLab02.ServiceClient ServiceClient = new SALLab02.ServiceClient();

            string StudentEmail = "martin2009@live.com";
            string password = "dsdddsdsd";
            string myDevice = Android.Provider.Settings.Secure.GetString(ContentResolver, Android.Provider.Settings.Secure.AndroidId);
            SALLab02.ResultInfo Result = await ServiceClient.ValidateAsync(StudentEmail, password, myDevice);
            Android.App.AlertDialog.Builder Builder = new AlertDialog.Builder(this);
            AlertDialog Alert = Builder.Create();
            Alert.SetTitle("Resultado de la verificacion");
            Alert.SetIcon(Resource.Drawable.Icon);
            Alert.SetMessage($"{Result.Status}\n{Result.Fullname}\n{Result.Token}");
            Alert.SetButton("OK", (s, ev) => { });
            Alert.Show();
        }




<TextView
        android:text="Proporcione un numero de telefono"
        android:textAppearance="?android:attr/textAppearanceLarge"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/textView1" />
    <EditText
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/PhoneNumberText"
        android:text="1-855-XAMARIN" />
    <Button
        android:text="Convertir"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/TranslateButton" />
    <Button
        android:text="Llamar"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/CallButton" />
    <Button
        android:text="@string/CallHistory"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/CallHistoryButton"
        android:enabled="false" />
    <Button
        android:text="Validar Actividad"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/ValidateButton" />













         <TextView
        android:text="Correo"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/textView1" />
    <EditText
        android:inputType="textEmailAddress"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/Email" />
    <TextView
        android:text="Contraseña"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/textView2" />
    <EditText
        android:inputType="textPassword"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/Password" />
    <Button
        android:text="Validar"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/ValidaButton" />
    <TextView
        android:text="Verificando...."
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/Verificador"
        android:textColor="@android:color/holo_blue_dark"
        android:scrollbarStyle="outsideInset"
        android:layout_marginLeft="110.0dp"
        android:layout_marginBottom="100.5dp" />







        using Android.App;
using Android.OS;
using Android.Widget;
namespace PhoneApp
{
    [Activity(Label = "PhoneApp-Decodificador", MainLauncher = true, Icon = "@drawable/icon")]
    public class MainActivity : Activity
    {
        
        protected override void OnCreate(Bundle bundle)
        {
            base.OnCreate(bundle);
            SetContentView(Resource.Layout.Main);
           

            // Set our view from the "main" layout resource
             

            
            var PhoneNumberText = FindViewById<EditText>(Resource.Id.PhoneNumberText);
            var TranslateButton = FindViewById<Button>(Resource.Id.TranslateButton);
            var CallButton = FindViewById<Button>(Resource.Id.CallButton);
            var CallHistoryButton = FindViewById<Button>(Resource.Id.CallHistoryButton);
          //  var ValidarButton= FindViewById<Button>(Resource.Id.ValidateButton);
            CallButton.Enabled = false;

            var TranslateNumber = string.Empty;
           
            TranslateButton.Click += (object sender, System.EventArgs e) =>
            {
                var Translator = new PhoneTranslator();
                TranslateNumber = Translator.ToNumber(PhoneNumberText.Text);
                if (string.IsNullOrWhiteSpace(TranslateNumber))
                {
                    //no hay numero a llamar
                    CallButton.Text = "Llamar";
                    CallButton.Enabled = false;
                }
                else
                {
                    //Hay un posible numero telefonico a Llamar
                    CallButton.Text = $"Llamar al {TranslateNumber}";
                    CallButton.Enabled = true;
                }

               
            };
            CallButton.Click += (object sender, System.EventArgs e) =>

            {
                //Intentar marcar el numero telefonico
                var CallDialog = new AlertDialog.Builder(this);
                CallDialog.SetMessage($"Llamar al numero {TranslateNumber}?");
                CallDialog.SetNeutralButton("Llamar", delegate
                {

                    //Agrega el numero marcado a la lista de numero marcado
                    PhoneNumbers.Add(TranslateNumber);
                    //Habilita el boton Call HistoryButton
                    CallHistoryButton.Enabled = true;


                    //Crear un intento para marcar el numero telefonico
                    var CallIntent = new Android.Content.Intent(Android.Content.Intent.ActionCall);
                    CallIntent.SetData(
                        Android.Net.Uri.Parse($"tel:{TranslateNumber}"));
                    StartActivity(CallIntent);

                });
                CallDialog.SetNegativeButton("Cancelar", delegate { });
                //Mostrar el cuadro de dialogo al usuario y esperar una respuesta.
                CallDialog.Show();
            };

            CallHistoryButton.Click += (sender, e) =>
            {
                var Intent = new Android.Content.Intent(this, typeof(CallHistoryActivity));
                Intent.PutStringArrayListExtra("phone_numbers", PhoneNumbers);
                StartActivity(Intent);
            };
           /* ValidarButton.Click += delegate {
                SetContentView(Resource.Layout.layoutValidate);
                Validate();
            };*/
        }
        private async void Validate()
        {
            var Verificador = FindViewById<TextView>(Resource.Id.Verificador);
            SALLab06.ServiceClient ServiceClient = new SALLab06.ServiceClient();

            string StudentEmail = "martin2009@live.com";
            string password = "espiritusanto23";
            string myDevice = Android.Provider.Settings.Secure.GetString(ContentResolver, Android.Provider.Settings.Secure.AndroidId);
            SALLab06.ResultInfo Result = await ServiceClient.ValidateAsync(StudentEmail, password, myDevice);
            /* Android.App.AlertDialog.Builder Builder = new AlertDialog.Builder(this);
             AlertDialog Alert = Builder.Create();
              Alert.SetTitle("Resultado de la verificacion");
              Alert.SetIcon(Resource.Drawable.Icon);
              Alert.SetMessage($"{Result.Status}\n{Result.Fullname}\n{Result.Token}");
              Alert.SetButton("OK", (s, ev) => { });

              Alert.Show();*/
            
            Verificador.Text= ($"{Result.Status}\n{Result.Fullname}\n{Result.Token}");
        }
        static readonly System.Collections.Generic.List<string> PhoneNumbers = new System.Collections.Generic.List<string>();
    }
   
}


