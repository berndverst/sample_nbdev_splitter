# AUTOGENERATED! DO NOT EDIT! File to edit: 00_create_test.ipynb (unless otherwise specified).

__all__ = ['test_fp', 'test_dataset', 'test_dataset', 'test_accuracy']

# Comes from mlops.ipynb, cell
test_fp = "iris_test.csv"

# Comes from mlops.ipynb, cell
test_dataset = tf.data.experimental.make_csv_dataset(
    test_fp,
    batch_size,
    column_names=column_names,
    label_name='species',
    num_epochs=1,
    shuffle=False)

test_dataset = test_dataset.map(pack_features_vector)

# Comes from mlops.ipynb, cell
test_accuracy = tf.keras.metrics.Accuracy()

for (x, y) in test_dataset:
  # training=False is needed only if there are layers with different
  # behavior during training versus inference (e.g. Dropout).
  logits = model(x, training=False)
  prediction = tf.argmax(logits, axis=1, output_type=tf.int32)
  test_accuracy(prediction, y)

print("Test set accuracy: {:.3%}".format(test_accuracy.result()))